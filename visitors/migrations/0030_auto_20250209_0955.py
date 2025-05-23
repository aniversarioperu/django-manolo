# Generated by Django 5.1.3 on 2025-02-09 14:55

from django.db import migrations


def update_insitutions(apps, schema_editor):
    Visitor = apps.get_model('visitors', 'Visitor')
    Institution = apps.get_model('visitors', 'Institution')

    list_of_institutions = [
        ("DESPACHO PRESIDENCIAL", "20161704378", "presidencia"),
        ("PRESIDENCIA DEL CONSEJO DE MINISTROS - PCM", "20168999926", "pcm"),
        ("MINISTERIO DEL AMBIENTE (MINAM)", "20492966658", "ambiente"),
        ("MINISTERIO DE ECONOMÍA Y FINANZAS (MEF)", "20131370645", "mef"),
        ("MINISTERIO DE JUSTICIA Y DERECHOS HUMANOS (MINJUS)", "20131371617", "minjus"),
        ("MINISTERIO DE DESARROLLO E INCLUSIÓN SOCIAL (MIDIS)", "20545565359", "midis"),
        ("MINISTERIO DE DESARROLLO AGRARIO Y RIEGO (MIDAGRI)", "20131372931", "minagr"),
        ("MINISTERIO DE COMERCIO EXTERIOR  Y TURISMO (MINCETUR)", "20504774288", "mincetur"),
        ("MINISTERIO DE EDUCACIÓN (MINEDU)", "20131370998", "minedu"),
        ("MINISTERIO DE ENERGÍA Y MINAS (MEM)", "20131368829", "minem"),
        ("MINISTERIO DE VIVIENDA, CONSTRUCCIÓN Y SANEAMIENTO (VIVIENDA)", "20504743307", "vivienda"),
        ("MINISTERIO DE TRANSPORTES Y COMUNICACIONES (MTC)", "20131379944", "mtc"),
        ("MINISTERIO DE LA MUJER Y POBLACIONES VULNERABLES (MIMP)", "20336951527", "min. mujer"),
        ("MINISTERIO DE LA PRODUCCIÓN (PRODUCE)", "20504794637", "produce"),
        ("MINISTERIO DE TRABAJO Y PROMOCIÓN DEL EMPLEO (MTPE)", "20131023414", "trabajo"),
        ("MINISTERIO DE CULTURA (CULTURA)", "20537630222", "mincu"),
        ("Organismo Supervisor de las Contrataciones del Estado", "20419026809", "osce"),
        ("Servicio de Agua Potable y Alcantarillado de Lima - Sedapal", "20100152356", "sedapal"),
        ("SUPERINTENDENCIA NACIONAL DE ADUANAS Y DE ADMINISTRACIÓN TRIBUTARIA (SUNAT)", "20131312955", "sunat"),
        ("MINISTERIO DE DEFENSA (MINDEF)", "20131367938", "defensa"),

        ("BANCO DE LA NACIÓN (BN)", "20100030595", "banco-nacion"),
        ("PETRÓLEOS DEL PERÚ (PETROPERU)", "20100128218", "petroperu"),
        ("SUPERINTENDENCIA DEL MERCADO DE VALORES (SMV)", "20131016396", "smv"),
        ("MINISTERIO DEL INTERIOR (MININTER)", "20131366966", "mininter"),
        ("EJÉRCITO DEL PERÚ (EP)", "20131369124", "ejercito"),
        ("INSTITUTO NACIONAL DE ESTADÍSTICA E INFORMÁTICA (INEI)", "20131369981", "inei"),
        ("INSTITUTO NACIONAL PENITENCIARIO (INPE)", "20131370050", "inpe"),
        ("MINISTERIO PÚBLICO FISCALÍA DE LA NACIÓN", "20131370301", "ministerio-publico"),
        ("SUPERINTENDENCIA DE BANCA, SEGUROS Y ADMINISTRADORAS PRIVADAS DE FONDOS DE PENSIONES", "20131370564", "sbs"),
        ("ARCHIVO GENERAL DE LA NACIÓN (AGN)", "20131370726", "agn"),
        ("COMISIÓN NACIONAL DE INVESTIGACIÓN Y DESARROLLO AEROESPACIAL (CONIDA)", "20131371889", "conida"),
        ("MINISTERIO DE SALUD (MINSA)", "20131373237", "minsa"),
        ("JURADO NACIONAL DE ELECCIONES", "20131378549", "jne"),
        ("LA CONTRALORÍA GENERAL DE LA REPÚBLICA", "20131378972", "contraloria"),
        ("MINISTERIO DE RELACIONES EXTERIORES (RREE)", "20131380101", "rree"),
        ("COMANDO CONJUNTO DE LAS FUERZAS ARMADAS (CCFFAA)", "20131380870", "ccffaa"),
        ("INSTITUTO PERUANO DEL DEPORTE (IPD)", "20135897044", "ipd"),
        ("FONDO NACIONAL DE DESARROLLO PESQUERO (FONDEPES)", "20137921601", "fondepes"),
        ("FUERZA AÉREA DEL PERÚ (FAP)", "20144364059", "fap"),
        ("MARINA DE GUERRA DEL PERÚ (MGP)", "20153408191", "mgp"),
        ("TRIBUNAL CONSTITUCIONAL", "20217267618", "tribunal-constitucional"),
        ("SUPERINTENDENCIA NACIONAL DE LOS REGISTROS PÚBLICOS (SUNARP)", "20267073580", "sunarp"),
        ("ACADEMIA DE LA MAGISTRATURA", "20290898685", "amag"),
        ("OFICINA NACIONAL DE PROCESOS ELECTORALES", "20291973851", "onpe"),
        ("REGISTRO NACIONAL DE IDENTIFICACIÓN Y ESTADO CIVIL", "20295613620", "reniec"),
        ("DEFENSORÍA DEL PUEBLO", "20304117142", "defensoria"),
        ("COMISIÓN DE PROMOCIÓN DEL PERÚ PARA LA EXPORTACIÓN Y EL TURISMO (PROMPERÚ)", "20307167442", "promperu"),
        ("INSTITUTO NACIONAL DE RADIO Y TELEVISIÓN DEL PERÚ (IRTP)", "20338915471", "irtp"),
        ("COMISIÓN NACIONAL PARA EL DESARROLLO Y VIDA SIN DROGAS (DEVIDA)", "20339267821", "devida"),
        ("INPE - OFICINA REGIONAL SUR (INPE - ORS)", "20370188131", "inpe-ors"),
        ("SUPERINTENDENCIA NACIONAL DE SALUD (SUSALUD)", "20377985843", "susalud"),
        ("AGENCIA DE PROMOCIÓN DE LA INVERSIÓN PRIVADA (PROINVERSION)", "20380799643", "proinversion"),
        ("FONDO MIVIVIENDA S. A. (FMV S.A.)", "20414671773", "fmv"),
        ("GOBIERNO REGIONAL DE LA LIBERTAD", "20440374248", "region-libertad"),
        ("GOBIERNO REGIONAL DE AYACUCHO", "20452393493", "region-ayacucho"),
        ("GOBIERNO REGIONAL DE ICA", "20452393817", "region-ica"),
        ("FONDO NACIONAL DE FINANCIAMIENTO DE LA ACTIVIDAD EMPRESARIAL DEL ESTADO (FONAFE)", "20458605662", "fonafe"),
        ("AUTORIDAD NACIONAL DEL SERVICIO CIVIL (SERVIR)", "20477906461", "servir"),
        ("GOBIERNO REGIONAL DE LAMBAYEQUE", "20479569780", "region-lambayeque"),
        ("GOBIERNO REGIONAL DE AMAZONAS", "20479569861", "region-amazonas"),
        ("GOBIERNO REGIONAL  TUMBES", "20484003883", "region-tumbes"),
        ("GOBIERNO REGIONAL PASCO", "20489252270", "region-pasco"),
        ("GOBIERNO REGIONAL DE LORETO", "20493196902", "region-loreto"),
        ("GOBIERNO REGIONAL DE AREQUIPA", "20498390570", "region-arequipa"),
        ("AGENCIA PERUANA DE COOPERACIÓN INTERNACIONAL (APCI)", "20504915523", "apci"),
        ("AUTORIDAD PORTUARIA NACIONAL (APN)", "20509645150", "apn"),
        ("GOBIERNO REGIONAL DE TACNA", "20519752515", "region-tacna"),
        ("CENTRO NACIONAL DE PLANEAMIENTO ESTRATÉGICO (CEPLAN)", "20520594451", "ceplan"),
        ("FUERO MILITAR POLICIAL (EX - CONSEJO SUPREMO DE JUSTICIA MILITAR)", "20520640071", "fuero-militar"),
        ("ORGANISMO DE EVALUACIÓN Y FISCALIZACIÓN AMBIENTAL (OEFA)", "20521286769", "oefa"),
        ("GOBIERNO REGIONAL DE APURIMAC", "20527141762", "region-apurimac"),
        ("GOBIERNO REGIONAL CUSCO", "20527147612", "region-cusco"),
        ("GOBIERNO REGIONAL DE LIMA", "20530688390", "region-lima"),
        ("GOBIERNO REGIONAL DE ANCASH", "20530689019", "region-ancash"),
        ("GOBIERNO REGIONAL SAN MARTÍN", "20531375808", "region-san-martin"),
        ("SUPERINTENDENCIA DE TRANSPORTE TERRESTRE DE PERSONAS, CARGA Y MERCANCIAS (SUTRAN)", "20536902385", "sutran"),
        ("CENTRO NACIONAL DE ABASTECIMIENTO DE RECURSOS ESTRATÉGICOS EN SALUD (CENARES)", "20538298485", "cenares"),
        ("SUPERINTENDENCIA NACIONAL DE MIGRACIONES (MIGRACIONES)", "20551239692", "migraciones"),
        ("AGENCIA DE COMPRAS DE LAS FUERZAS ARMADAS (ACFFAA)", "20556939781", "acffaa"),
        ("SUPERINTENDENCIA NACIONAL DE EDUCACION SUPERIOR UNIVERSITARIA (SUNEDU)", "20600044975", "sunedu"),
        ("CENTRAL DE COMPRAS PÚBLICAS - PERÚ COMPRAS (PERÚ COMPRAS)", "20600927818", "peru-compras"),
        ("AUTORIDAD DE TRANSPORTE URBANO PARA LIMA Y CALLAO - ATU", "20604932964", "atu"),
        ("AUTORIDAD NACIONAL DE INFRAESTRUCTURA", "20611816953", "ani"),
    ]
    for i in list_of_institutions:
        name, ruc, slug = i
        print(name, ruc, slug)
        institution, _ = Institution.objects.get_or_create(slug=slug)
        institution.name = name
        institution.ruc = ruc
        institution.slug = slug
        institution.save()

    visitors = Visitor.objects.all().order_by("id")
    institutions = {inst.slug: inst for inst in Institution.objects.all()}

    total = visitors.count()
    count = 0
    chunk_size = 1_000
    for i in range(0, total, chunk_size):
        chunk = visitors[i:i + chunk_size]
        for visitor in chunk:
            visitor.institution2 = institutions[visitor.institution]
        Visitor.objects.bulk_update(chunk, ['institution2'])
        count += chunk_size
        print(f"Updated {count} of {total}")


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0029_institution_ruc"),
    ]

    operations = [
        migrations.RunPython(
            update_insitutions, reverse_code=migrations.RunPython.noop
        ),
    ]
