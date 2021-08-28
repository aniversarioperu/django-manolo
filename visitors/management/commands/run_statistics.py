import json
import math

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Count
from django.utils import timezone
from twitterbot.bot import TwitterBot

from visitors.models import Visitor, Statistic, Statistic_detail, Institution, VisitorScrapeProgress


class Command(BaseCommand):
    help = 'calculates the five people that visited the most'

    def handle(self, *args, **options):

        print("Doing calculations")
        run_statistics()


def run_statistics():
    # all_visitor_names = Visitor.objects.all().exclude(full_name=",").values_list(
    #     "full_name", flat=True,
    # )
    # all_visitor_names_unique = set(all_visitor_names)
    # print(len(all_visitor_names_unique))
    #
    # visitors = Visitor.objects.all().exclude(full_name=",").values_list(
    #     "full_name",
    # ).annotate(
    #     the_count=Count("full_name"),
    # ).order_by(
    #     '-the_count',
    # )[:50]

    # Statistic_detail.objects.all().delete()
    # names_and_visits = []
    # for visitor in visitors:
    #     visit = Statistic_detail(name=visitor[0], number_of_visits=visitor[1])
    #     names_and_visits.append(visit)
    # Statistic_detail.objects.bulk_create(names_and_visits)

    # ls = []
    # data_dict = {"name": "Statistics", "children": ls}
    #
    # for i in visitors:
    #     dic = {"name": i[0], "children": []}
    #     ls.append(dic)
    #     institution = Visitor.objects.filter(
    #         full_name=i[0],
    #     ).values_list("institution").annotate(the_count=Count("institution"))
    #     for j in institution:
    #         dic_2 = {"name": j[0], "children": []}
    #         dic["children"].append(dic_2)
    #
    #     nombre = [d for d in ls if d['name'] == i[0]]
    #
    #     cuenta = 0
    #     while cuenta < len(institution):
    #         reason = Visitor.objects.filter(
    #             full_name=i[0],
    #             institution=institution[cuenta][0],
    #         ).values_list("reason").annotate(the_count=Count("reason"))
    #         for l in reason:
    #             dic_3 = {"name": l[0], "size": l[1]}
    #             nombre[0]['children'][cuenta]['children'].append(dic_3)
    #         cuenta += 1
    # print("Deleting data in Statistics")
    # Statistic.objects.all().delete()

    # stats = store_total_visitor_count(data_dict)
    stats = Statistic.objects.last()
    store_updated_institutions(stats)

    number_of_rows = Statistic.objects.all().count()
    print("Currently have {} rows in Statistics".format(number_of_rows))


def store_total_visitor_count(data_dict):
    print("Saving data to Statistics")
    stats = Statistic.objects.create(data=json.dumps(data_dict))
    stats.visitor_count = Visitor.objects.all().count()
    stats.save()

    last_entry = VisitorScrapeProgress.objects.last()

    if last_entry:
        last_entry_millions = math.floor(last_entry.visitor_count / 1_000_000)
        current_count_millions = math.floor(stats.visitor_count / 1_000_000)
        if current_count_millions - last_entry_millions > 0:
            twitter = TwitterBot(
                settings.TWITTER_CONSUMER_KEY,
                settings.TWITTER_CONSUMER_SECRET,
                settings.TWITTER_OAUTH_TOKEN,
                settings.TWITTER_OAUTH_TOKEN_SECRET,
            )
            twitter.send_tweet(
                f'la base de datos de manolo.rocks sobrepasó los {current_count_millions} millones '
                f'de registros de visitas con {stats.visitor_count:,} registros'
            )

    if not VisitorScrapeProgress.objects.filter(cutoff_date=timezone.now()).exists():
        VisitorScrapeProgress.objects.create(
            visitor_count=stats.visitor_count,
            cutoff_date=timezone.now(),
        )

    return stats


def store_updated_institutions(stats):
    institution_stats = []

    for institution in Institution.objects.all().order_by('-rank'):
        last_visitor = Visitor.objects.filter(
            institution=institution.slug,
        ).order_by('date').last()

        if last_visitor:
            item = {
                'name': institution.name,
                'slug': institution.slug,
                'rank': institution.rank,
                'last_updated': last_visitor.date.strftime('%Y-%m-%d'),
            }
            institution_stats.append(item)

    stats.updated_institutions = institution_stats
    stats.save()
