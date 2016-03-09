# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160302_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=63, choices=[('ab', 'Abkhazian'), ('ace', 'Achinese'), ('ach', 'Acoli'), ('ada', 'Adangme'), ('ady', 'Adyghe'), ('aa', 'Afar'), ('afh', 'Afrihili'), ('af', 'Afrikaans'), ('agq', 'Aghem'), ('ain', 'Ainu'), ('ak', 'Akan'), ('akk', 'Akkadian'), ('bss', 'Akoose'), ('akz', 'Alabama'), ('sq', 'Albanian'), ('ale', 'Aleut'), ('arq', 'Algerian arabic'), ('ase', 'American sign language'), ('am', 'Amharic'), ('egy', 'Ancient egyptian'), ('grc', 'Ancient greek'), ('anp', 'Angika'), ('njo', 'Ao naga'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('arc', 'Aramaic'), ('aro', 'Araona'), ('arp', 'Arapaho'), ('arw', 'Arawak'), ('hy', 'Armenian'), ('rup', 'Aromanian'), ('frp', 'Arpitan'), ('as', 'Assamese'), ('ast', 'Asturian'), ('asa', 'Asu'), ('cch', 'Atsam'), ('av', 'Avaric'), ('ae', 'Avestan'), ('awa', 'Awadhi'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bfq', 'Badaga'), ('ksf', 'Bafia'), ('bfd', 'Bafut'), ('bqi', 'Bakhtiari'), ('ban', 'Balinese'), ('bal', 'Baluchi'), ('bm', 'Bambara'), ('bax', 'Bamun'), ('bjn', 'Banjar'), ('bas', 'Basaa'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bbc', 'Batak toba'), ('bar', 'Bavarian'), ('bej', 'Beja'), ('be', 'Belarusian'), ('bem', 'Bemba'), ('bez', 'Bena'), ('bn', 'Bengali'), ('bew', 'Betawi'), ('bho', 'Bhojpuri'), ('bik', 'Bikol'), ('bin', 'Bini'), ('bpy', 'Bishnupriya'), ('bi', 'Bislama'), ('byn', 'Blin'), ('zbl', 'Blissymbols'), ('brx', 'Bodo'), ('bs', 'Bosnian'), ('brh', 'Brahui'), ('bra', 'Braj'), ('pt_BR', 'Brazilian portuguese'), ('br', 'Breton'), ('bug', 'Buginese'), ('bg', 'Bulgarian'), ('bum', 'Bulu'), ('bua', 'Buriat'), ('my', 'Burmese'), ('cad', 'Caddo'), ('frc', 'Cajun french'), ('yue', 'Cantonese'), ('cps', 'Capiznon'), ('car', 'Carib'), ('ca', 'Catalan'), ('cay', 'Cayuga'), ('ceb', 'Cebuano'), ('tzm', 'Central atlas tamazight'), ('dtp', 'Central dusun'), ('ckb', 'Central kurdish'), ('esu', 'Central yupik'), ('shu', 'Chadian arabic'), ('chg', 'Chagatai'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('chr', 'Cherokee'), ('chy', 'Cheyenne'), ('chb', 'Chibcha'), ('cgg', 'Chiga'), ('qug', 'Chimborazo highland quichua'), ('zh', 'Chinese'), ('chn', 'Chinook jargon'), ('chp', 'Chipewyan'), ('cho', 'Choctaw'), ('cu', 'Church slavic'), ('chk', 'Chuukese'), ('cv', 'Chuvash'), ('nwc', 'Classical newari'), ('syc', 'Classical syriac'), ('ksh', 'Colognian'), ('swb', 'Comorian'), ('swc', 'Congo swahili'), ('cop', 'Coptic'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('mus', 'Creek'), ('crh', 'Crimean turkish'), ('hr', 'Croatian'), ('cs', 'Czech'), ('dak', 'Dakota'), ('da', 'Danish'), ('dar', 'Dargwa'), ('fa_AF', 'Dari'), ('dzg', 'Dazaga'), ('del', 'Delaware'), ('din', 'Dinka'), ('dv', 'Divehi'), ('doi', 'Dogri'), ('dgr', 'Dogrib'), ('dua', 'Duala'), ('nl', 'Dutch'), ('dyu', 'Dyula'), ('dz', 'Dzongkha'), ('frs', 'Eastern frisian'), ('efi', 'Efik'), ('arz', 'Egyptian arabic'), ('eka', 'Ekajuk'), ('elx', 'Elamite'), ('ebu', 'Embu'), ('egl', 'Emilian'), ('en', 'English'), ('myv', 'Erzya'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('pt_PT', 'European portuguese'), ('es_ES', 'European spanish'), ('ee', 'Ewe'), ('ewo', 'Ewondo'), ('ext', 'Extremaduran'), ('fan', 'Fang'), ('fat', 'Fanti'), ('fo', 'Faroese'), ('hif', 'Fiji hindi'), ('fj', 'Fijian'), ('fil', 'Filipino'), ('fi', 'Finnish'), ('nl_BE', 'Flemish'), ('fon', 'Fon'), ('gur', 'Frafra'), ('fr', 'French'), ('fur', 'Friulian'), ('ff', 'Fulah'), ('gaa', 'Ga'), ('gag', 'Gagauz'), ('gl', 'Galician'), ('gan', 'Gan chinese'), ('lg', 'Ganda'), ('gay', 'Gayo'), ('gba', 'Gbaya'), ('gez', 'Geez'), ('ka', 'Georgian'), ('de', 'German'), ('aln', 'Gheg albanian'), ('bbj', 'Ghomala'), ('glk', 'Gilaki'), ('gil', 'Gilbertese'), ('gom', 'Goan konkani'), ('gon', 'Gondi'), ('gor', 'Gorontalo'), ('got', 'Gothic'), ('grb', 'Grebo'), ('el', 'Greek'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('guz', 'Gusii'), ('gwi', 'Gwich\u02bcin'), ('hai', 'Haida'), ('ht', 'Haitian creole'), ('hak', 'Hakka chinese'), ('ha', 'Hausa'), ('haw', 'Hawaiian'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hil', 'Hiligaynon'), ('hi', 'Hindi'), ('ho', 'Hiri motu'), ('hit', 'Hittite'), ('hmn', 'Hmong'), ('hu', 'Hungarian'), ('hup', 'Hupa'), ('iba', 'Iban'), ('ibb', 'Ibibio'), ('is', 'Icelandic'), ('io', 'Ido'), ('ig', 'Igbo'), ('ilo', 'Iloko'), ('smn', 'Inari sami'), ('id', 'Indonesian'), ('izh', 'Ingrian'), ('inh', 'Ingush'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiaq'), ('ga', 'Irish'), ('it', 'Italian'), ('jam', 'Jamaican creole english'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kaj', 'Jju'), ('dyo', 'Jola-fonyi'), ('jrb', 'Judeo-arabic'), ('jpr', 'Judeo-persian'), ('jut', 'Jutish'), ('kbd', 'Kabardian'), ('kea', 'Kabuverdianu'), ('kab', 'Kabyle'), ('kac', 'Kachin'), ('kgp', 'Kaingang'), ('kkj', 'Kako'), ('kl', 'Kalaallisut'), ('kln', 'Kalenjin'), ('xal', 'Kalmyk'), ('kam', 'Kamba'), ('kbl', 'Kanembu'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('kaa', 'Kara-kalpak'), ('krc', 'Karachay-balkar'), ('krl', 'Karelian'), ('ks', 'Kashmiri'), ('csb', 'Kashubian'), ('kaw', 'Kawi'), ('kk', 'Kazakh'), ('ken', 'Kenyang'), ('kha', 'Khasi'), ('km', 'Khmer'), ('kho', 'Khotanese'), ('khw', 'Khowar'), ('ki', 'Kikuyu'), ('kmb', 'Kimbundu'), ('krj', 'Kinaray-a'), ('rw', 'Kinyarwanda'), ('kiu', 'Kirmanjki'), ('tlh', 'Klingon'), ('bkm', 'Kom'), ('kv', 'Komi'), ('koi', 'Komi-permyak'), ('kg', 'Kongo'), ('kok', 'Konkani'), ('ko', 'Korean'), ('kfo', 'Koro'), ('kos', 'Kosraean'), ('avk', 'Kotava'), ('khq', 'Koyra chiini'), ('ses', 'Koyraboro senni'), ('kpe', 'Kpelle'), ('kri', 'Krio'), ('kj', 'Kuanyama'), ('kum', 'Kumyk'), ('ku', 'Kurdish'), ('kru', 'Kurukh'), ('kut', 'Kutenai'), ('nmg', 'Kwasio'), ('ky', 'Kyrgyz'), ('quc', 'K\u02bciche\u02bc'), ('lad', 'Ladino'), ('lah', 'Lahnda'), ('lkt', 'Lakota'), ('lam', 'Lamba'), ('lag', 'Langi'), ('lo', 'Lao'), ('ltg', 'Latgalian'), ('la', 'Latin'), ('es_419', 'Latin american spanish'), ('lv', 'Latvian'), ('lzz', 'Laz'), ('lez', 'Lezghian'), ('lij', 'Ligurian'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lfn', 'Lingua franca nova'), ('lzh', 'Literary chinese'), ('lt', 'Lithuanian'), ('liv', 'Livonian'), ('jbo', 'Lojban'), ('lmo', 'Lombard'), ('nds', 'Low german'), ('nds_NL', 'Low saxon'), ('sli', 'Lower silesian'), ('dsb', 'Lower sorbian'), ('loz', 'Lozi'), ('lu', 'Luba-katanga'), ('lua', 'Luba-lulua'), ('lui', 'Luiseno'), ('smj', 'Lule sami'), ('lun', 'Lunda'), ('luo', 'Luo'), ('lb', 'Luxembourgish'), ('luy', 'Luyia'), ('mde', 'Maba'), ('mk', 'Macedonian'), ('jmc', 'Machame'), ('mad', 'Madurese'), ('maf', 'Mafa'), ('mag', 'Magahi'), ('vmf', 'Main-franconian'), ('mai', 'Maithili'), ('mak', 'Makasar'), ('mgh', 'Makhuwa-meetto'), ('kde', 'Makonde'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mnc', 'Manchu'), ('mdr', 'Mandar'), ('man', 'Mandingo'), ('mni', 'Manipuri'), ('gv', 'Manx'), ('mi', 'Maori'), ('arn', 'Mapuche'), ('mr', 'Marathi'), ('chm', 'Mari'), ('mh', 'Marshallese'), ('mwr', 'Marwari'), ('mas', 'Masai'), ('mzn', 'Mazanderani'), ('byv', 'Medumba'), ('men', 'Mende'), ('mwv', 'Mentawai'), ('mer', 'Meru'), ('mgo', 'Meta\u02bc'), ('es_MX', 'Mexican spanish'), ('mic', 'Micmac'), ('dum', 'Middle dutch'), ('enm', 'Middle english'), ('frm', 'Middle french'), ('gmh', 'Middle high german'), ('mga', 'Middle irish'), ('nan', 'Min nan chinese'), ('min', 'Minangkabau'), ('xmf', 'Mingrelian'), ('mwl', 'Mirandese'), ('lus', 'Mizo'), ('ar_001', 'Modern standard arabic'), ('moh', 'Mohawk'), ('mdf', 'Moksha'), ('ro_MD', 'Moldavian'), ('lol', 'Mongo'), ('mn', 'Mongolian'), ('mfe', 'Morisyen'), ('ary', 'Moroccan arabic'), ('mos', 'Mossi'), ('mua', 'Mundang'), ('ttt', 'Muslim tat'), ('mye', 'Myene'), ('naq', 'Nama'), ('na', 'Nauru'), ('nv', 'Navajo'), ('ng', 'Ndonga'), ('nap', 'Neapolitan'), ('ne', 'Nepali'), ('new', 'Newari'), ('sba', 'Ngambay'), ('nnh', 'Ngiemboon'), ('jgo', 'Ngomba'), ('yrl', 'Nheengatu'), ('nia', 'Nias'), ('niu', 'Niuean'), ('nog', 'Nogai'), ('nd', 'North ndebele'), ('frr', 'Northern frisian'), ('lrc', 'Northern luri'), ('se', 'Northern sami'), ('nso', 'Northern sotho'), ('no', 'Norwegian'), ('nb', 'Norwegian bokm\xe5l'), ('nn', 'Norwegian nynorsk'), ('nov', 'Novial'), ('nus', 'Nuer'), ('nym', 'Nyamwezi'), ('ny', 'Nyanja'), ('nyn', 'Nyankole'), ('tog', 'Nyasa tonga'), ('nyo', 'Nyoro'), ('nzi', 'Nzima'), ('nqo', 'N\u2019ko'), ('oc', 'Occitan'), ('oj', 'Ojibwa'), ('ang', 'Old english'), ('fro', 'Old french'), ('goh', 'Old high german'), ('sga', 'Old irish'), ('non', 'Old norse'), ('peo', 'Old persian'), ('pro', 'Old proven\xe7al'), ('or', 'Oriya'), ('om', 'Oromo'), ('osa', 'Osage'), ('os', 'Ossetic'), ('ota', 'Ottoman turkish'), ('pal', 'Pahlavi'), ('pfl', 'Palatine german'), ('pau', 'Palauan'), ('pi', 'Pali'), ('pam', 'Pampanga'), ('pag', 'Pangasinan'), ('pap', 'Papiamento'), ('ps', 'Pashto'), ('pdc', 'Pennsylvania german'), ('fa', 'Persian'), ('phn', 'Phoenician'), ('pcd', 'Picard'), ('pms', 'Piedmontese'), ('pdt', 'Plautdietsch'), ('pon', 'Pohnpeian'), ('pl', 'Polish'), ('pnt', 'Pontic'), ('pt', 'Portuguese'), ('prg', 'Prussian'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('raj', 'Rajasthani'), ('rap', 'Rapanui'), ('rar', 'Rarotongan'), ('rif', 'Riffian'), ('rgn', 'Romagnol'), ('ro', 'Romanian'), ('rm', 'Romansh'), ('rom', 'Romany'), ('rof', 'Rombo'), ('root', 'Root'), ('rtm', 'Rotuman'), ('rug', 'Roviana'), ('rn', 'Rundi'), ('ru', 'Russian'), ('rue', 'Rusyn'), ('rwk', 'Rwa'), ('ssy', 'Saho'), ('sah', 'Sakha'), ('sam', 'Samaritan aramaic'), ('saq', 'Samburu'), ('sm', 'Samoan'), ('sgs', 'Samogitian'), ('sad', 'Sandawe'), ('sg', 'Sango'), ('sbp', 'Sangu'), ('sa', 'Sanskrit'), ('sat', 'Santali'), ('sc', 'Sardinian'), ('sas', 'Sasak'), ('sdc', 'Sassarese sardinian'), ('stq', 'Saterland frisian'), ('saz', 'Saurashtra'), ('sco', 'Scots'), ('gd', 'Scottish gaelic'), ('sly', 'Selayar'), ('sel', 'Selkup'), ('seh', 'Sena'), ('see', 'Seneca'), ('sr', 'Serbian'), ('sh', 'Serbo-croatian'), ('srr', 'Serer'), ('sei', 'Seri'), ('ksb', 'Shambala'), ('shn', 'Shan'), ('sn', 'Shona'), ('ii', 'Sichuan yi'), ('scn', 'Sicilian'), ('sid', 'Sidamo'), ('bla', 'Siksika'), ('szl', 'Silesian'), ('zh_Hans', 'Simplified chinese'), ('sd', 'Sindhi'), ('si', 'Sinhala'), ('sms', 'Skolt sami'), ('den', 'Slave'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('xog', 'Soga'), ('sog', 'Sogdien'), ('so', 'Somali'), ('snk', 'Soninke'), ('nr', 'South ndebele'), ('alt', 'Southern altai'), ('sdh', 'Southern kurdish'), ('sma', 'Southern sami'), ('st', 'Southern sotho'), ('es', 'Spanish'), ('srn', 'Sranan tongo'), ('zgh', 'Standard moroccan tamazight'), ('suk', 'Sukuma'), ('sux', 'Sumerian'), ('su', 'Sundanese'), ('sus', 'Susu'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('gsw', 'Swiss german'), ('syr', 'Syriac'), ('shi', 'Tachelhit'), ('tl', 'Tagalog'), ('ty', 'Tahitian'), ('dav', 'Taita'), ('tg', 'Tajik'), ('tly', 'Talysh'), ('tmh', 'Tamashek'), ('ta', 'Tamil'), ('trv', 'Taroko'), ('twq', 'Tasawaq'), ('tt', 'Tatar'), ('te', 'Telugu'), ('ter', 'Tereno'), ('teo', 'Teso'), ('tet', 'Tetum'), ('th', 'Thai'), ('bo', 'Tibetan'), ('tig', 'Tigre'), ('ti', 'Tigrinya'), ('tem', 'Timne'), ('tiv', 'Tiv'), ('tli', 'Tlingit'), ('tpi', 'Tok pisin'), ('tkl', 'Tokelau'), ('to', 'Tongan'), ('fit', 'Tornedalen finnish'), ('zh_Hant', 'Traditional chinese'), ('tkr', 'Tsakhur'), ('tsd', 'Tsakonian'), ('tsi', 'Tsimshian'), ('ts', 'Tsonga'), ('tn', 'Tswana'), ('tcy', 'Tulu'), ('tum', 'Tumbuka'), ('aeb', 'Tunisian arabic'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tru', 'Turoyo'), ('tvl', 'Tuvalu'), ('tyv', 'Tuvinian'), ('tw', 'Twi'), ('kcg', 'Tyap'), ('udm', 'Udmurt'), ('uga', 'Ugaritic'), ('uk', 'Ukrainian'), ('umb', 'Umbundu'), ('hsb', 'Upper sorbian'), ('ur', 'Urdu'), ('ug', 'Uyghur'), ('uz', 'Uzbek'), ('vai', 'Vai'), ('ve', 'Venda'), ('vec', 'Venetian'), ('vep', 'Veps'), ('vi', 'Vietnamese'), ('vo', 'Volap\xfck'), ('vot', 'Votic'), ('vun', 'Vunjo'), ('vro', 'V\xf5ro'), ('wa', 'Walloon'), ('wae', 'Walser'), ('war', 'Waray'), ('wbp', 'Warlpiri'), ('was', 'Washo'), ('guc', 'Wayuu'), ('cy', 'Welsh'), ('vls', 'West flemish'), ('bgn', 'Western balochi'), ('fy', 'Western frisian'), ('mrj', 'Western mari'), ('wal', 'Wolaytta'), ('wo', 'Wolof'), ('wuu', 'Wu chinese'), ('xh', 'Xhosa'), ('hsn', 'Xiang chinese'), ('yav', 'Yangben'), ('yao', 'Yao'), ('yap', 'Yapese'), ('ybb', 'Yemba'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zap', 'Zapotec'), ('dje', 'Zarma'), ('zza', 'Zaza'), ('zea', 'Zeelandic'), ('zen', 'Zenaga'), ('za', 'Zhuang'), ('gbz', 'Zoroastrian dari'), ('zu', 'Zulu'), ('zun', 'Zuni')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
