from scrapy import Request

from scrapers.manolo_scraper.spiders.spiders import ManoloBaseSpider
from ..items import ManoloItem
from ..item_loaders import ManoloItemLoader
from ..utils import make_hash, get_dni


class TrabajoSpiderOld(ManoloBaseSpider):
    name = 'trabajo_old'
    allowed_domains = ['visitas.trabajo.gob.pe']
    NUMBER_OF_PAGES_PER_PAGE = 10
    base_url = "http://visitas.trabajo.gob.pe/portalvisitas/lista.htm"

    def initial_request(self, date):
        date_str = date.strftime("%d/%m/%Y")

        # This initial request always hits the current page of the date.
        request = Request(
            url=f"{self.base_url}?inicioFilter={date_str}&finalFilter={date_str}",
            meta={
                'date': date_str,
            },
            dont_filter=True,
            callback=self.parse)

        return request

    def parse(self, response, **kwargs):
        date = self.get_date_item(response.meta['date'], '%d/%m/%Y')

        for row in response.xpath('//tr'):
            data = row.xpath('td')

            try:
                full_name = data[1].xpath('text()').extract_first()
            except IndexError:
                continue

            if full_name.strip():
                dni = data[2].xpath('text()').extract_first()
                id_document, id_number = get_dni(dni)

                loader = ManoloItemLoader(item=ManoloItem(), selector=row)
                loader.add_value('institution', self.name)
                loader.add_value('date', date)
                loader.add_value('full_name', full_name)

                loader.add_value('id_document', id_document)
                loader.add_value('id_number', id_number)
                loader.add_xpath('entity', './td[4]/text()')
                loader.add_xpath('reason', './td[5]/text()')
                loader.add_xpath('host_name', './td[6]/text()')
                loader.add_xpath('meeting_place', './td[7]/text()')
                loader.add_xpath('office', './td[8]/text()')
                loader.add_xpath('time_start', './td[9]/text()')
                loader.add_xpath('time_end', './td[10]/text()')

                item = loader.load_item()
                item = make_hash(item)

                yield item
