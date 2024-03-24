import json

import scrapy
from scrapy import Request

from .spiders import ManoloBaseSpider
from ..item_loaders import ManoloItemLoader
from ..items import ManoloItem
from ..utils import make_hash


class MujerSpiderOld(ManoloBaseSpider):
    name = 'mujer'
    allowed_domains = ['appweb.mimp.gob.pe']

    custom_settings = {
        'DOWNLOAD_DELAY': '25',
        'RETRY_TIMES': '10',
    }
    base_url = 'https://appweb.mimp.gob.pe:8181/visitas-web/faces/reportes/listado/reporteTransparenciaVisitas.xhtml'  # noqa
    NUMBER_OF_ITEMS_PER_PAGE = 20

    def initial_request(self, date):
        date_str = date.strftime('%d/%m/%Y')
        return Request(
            url=self.base_url,
            dont_filter=True,
            meta={
                'date': date_str,
                'retry': 1,
            },
            callback=self.parse_initial_request,
        )

    def parse_initial_request(self, response):
        date_str = response.meta['date']
        view_state = response.xpath("//input[@name='javax.faces.ViewState']/@value").extract_first()
        print('***** parase intiial request')

        params = {
            "javax.faces.partial.ajax": "true",
            "javax.faces.source": "j_idt13:j_idt24",
            "javax.faces.partial.execute": "@all",
            "javax.faces.partial.render": "j_idt13:tablaReporteVisita",
            "j_idt13:j_idt24": "j_idt13:j_idt24",
            "j_idt13": "j_idt13",
            "j_idt13:tipoBusquedaFecha_focus": "",
            "j_idt13:tipoBusquedaFecha_input": "range",
            "j_idt13:primeraFecha_input": date_str,
            "j_idt13:segundaFecha_input": date_str,
            "j_idt13:tablaReporteVisita:j_idt32:filter": "",
            "j_idt13:tablaReporteVisita:j_idt34:filter": "",
            "j_idt13:tablaReporteVisita:j_idt36:filter": "",
            "j_idt13:tablaReporteVisita:j_idt38:filter": "",
            "j_idt13:tablaReporteVisita:j_idt40:filter": "",
            "j_idt13:tablaReporteVisita:j_idt42:filter": "",
            "javax.faces.ViewState": view_state,
        }
        print(params)
        return scrapy.FormRequest(
            url=self.base_url,
            formdata=params,
            meta={
                'date': date_str,
                'retry':  1,
            },
            dont_filter=True,
            callback=self.parse,
        )

    def parse(self, response, **kwargs):
        data = json.loads(response.body)
        rows = data['rows']

        for row in rows:
            loader = ManoloItemLoader(item=ManoloItem())

            item_date = row.get('fec_fecha', '')
            if item_date:
                item_date = self.get_date_item(item_date, '%d/%m/%Y')
            loader.add_value('institution', 'min. mujer')
            loader.add_value('date', item_date)
            loader.add_value('full_name', row['txt_nombre_visitante'])
            loader.add_value('id_number', row['txt_dni'])
            loader.add_value('id_document', 'DNI')
            loader.add_value('entity', row['txt_entidad'])
            loader.add_value('reason', row['txt_observacion'])
            loader.add_value('host_name', row['txt_nombre_funcionario'])
            loader.add_value('office', row['txt_unidad'])
            loader.add_value('time_start', row['ingreso'])
            loader.add_value('time_end', row['salida'])

            item = loader.load_item()

            item = make_hash(item)
            yield item
