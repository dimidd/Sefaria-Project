# -*- coding: utf-8 -*-

import pytest
import pprint
from sefaria.model import *
from sefaria.system.exceptions import InputError


class Test_Schema(object):
    def test_schema_load(self):
        i = Index().load({"title": "Mishnah Torah Test"})
        if i:
            i.delete()
        schema = {
            "key": "Mishnah Torah Test",
            "titles": [
                {
                    "lang": "en",
                    "text": "Mishnah Torah Test",
                    "primary": True
                },
                {
                    "lang": "en",
                    "text": "Rambam Test"
                },
                {
                    "lang": "he",
                    "text": u"משנה תורה כאילו",
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Introduction",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Introduction",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u"הקדמה",
                            "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "Transmission",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Transmission",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "depth": 1,
                            "addressTypes": ["Integer"],
                            "sectionNames": ["Paragraph"]
                        },
                        {
                            "key": "List of Positive Mitzvot",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "List of Positive Mitzvot",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "depth": 1,
                            "addressTypes": ["Integer"],
                            "sectionNames": ["Mitzvah"]
                        },
                        {
                            "key": "List of Negative Mitzvot",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "List of Negative Mitzvot",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "depth": 1,
                            "addressTypes": ["Integer"],
                            "sectionNames": ["Mitzvah"]
                        }
                    ]

                },
                {
                    "key": "Sefer Mada",
                    "titles": [
                        {
                        "lang": "en",
                        "text": "Sefer Mada",
                        "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "Foundations of the Torah",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Foundations of the Torah",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 0,
                                    "addressTypes": [],
                                    "sectionNames": []
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 2,
                                    "addressTypes": ["Integer", "Integer"],
                                    "sectionNames": ["Chapter", "Law"]
                                }
                            ]
                        },
                        {
                            "key": "Human Dispositions",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Human Dispositions",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 0,
                                    "addressTypes": [],
                                    "sectionNames": []
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 2,
                                    "addressTypes": ["Integer", "Integer"],
                                    "sectionNames": ["Chapter", "Law"]
                                }
                            ]
                        },
                        {
                            "key": "Torah Study",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Torah Study",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 0,
                                    "addressTypes": [],
                                    "sectionNames": []
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 2,
                                    "addressTypes": ["Integer", "Integer"],
                                    "sectionNames": ["Chapter", "Law"]
                                }
                            ]
                        },
                        {
                            "key": "Foreign Worship and Customs of the Nations",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Foreign Worship and Customs of the Nations",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 0,
                                    "addressTypes": [],
                                    "sectionNames": []
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 2,
                                    "addressTypes": ["Integer", "Integer"],
                                    "sectionNames": ["Chapter", "Law"]
                                }
                            ]
                        },
                        {
                            "key": "Repentance",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Repentance",
                                "primary": True
                                },
                                {
                                "lang": "en",
                                "text": "Hilchot Teshuva",
                                "presentation": "alone"
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 0,
                                    "addressTypes": [],
                                    "sectionNames": []
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "depth": 2,
                                    "addressTypes": ["Integer", "Integer"],
                                    "sectionNames": ["Chapter", "Law"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        i = Index({
            "schema": schema,
            "title": "Mishnah Torah Test",
            "categories": ["Halakhah"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        schema['titles'] = sorted(schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert schema == serialized

        Ref("Mishnah Torah Test, Introduction, Transmission")

        with pytest.raises(InputError):
            Ref("Mishnah Torah Test, Introduction, TransmisXsion")  # Mispelled last piece

        i.delete()


    def test_schema_load_2(self):
        i = Index().load({"title": "Lekutei Moharan"})
        if i:
            i.delete()
        lm_schema = {
            "key": "Lekutei Moharan",
            "titles": [
                {
                    "lang": "en",
                    "text": "Lekutei Moharan",
                    "primary": True
                },
                {
                    "lang": "en",
                    "text": "Likutey Moharan"
                },
                {
                    "lang": "en",
                    "text": "Likkutei Moharan"
                },
                {
                    "lang": "he",
                    "text": u'ליקוטי מוהרן',  # took the " out from before final nun to avoid name conflict
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Approbations",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Approbations",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u'הסכמות',
                            "primary": True
                        }
                    ],
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Approbation"]
                },
                {
                    "key": "Introduction",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Introduction",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u"הקדמה",
                            "primary": True
                        }
                    ],
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Paragraph"]
                },
                {
                    "key": "default",
                    "default": True,
                    "nodeType": "JaggedArrayNode",
                    "depth": 3,
                    "addressTypes": ["Integer", "Integer", "Integer"],
                    "sectionNames": ["Torah", "Section", "Paragraph"]
                },
                {
                    "key": "Tanina",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Tanina",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u'תנינא',
                            "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "default",
                            "default": True,
                            "nodeType": "JaggedArrayNode",
                            "depth": 3,
                            "addressTypes": ["Integer", "Integer", "Integer"],
                            "sectionNames": ["Torah", "Section", "Paragraph"]
                        },
                        {
                            "key": "Letters",
                            "titles" : [
                                {
                                    "lang": "en",
                                    "text": "Letters",
                                    "primary": True
                                },
                                {
                                    "lang": "he",
                                    "text": u'מכתב יד',
                                    "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "depth": 2,
                            "addressTypes": ["Integer", "Integer"],
                            "sectionNames": ["Letter", "Paragraph"]
                        }
                    ]
                }
            ]
        }
        i = Index({
            "schema": lm_schema,
            "title": "Lekutei Moharan",
            "categories": ["Chasidut"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        lm_schema['titles'] = sorted(lm_schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert lm_schema == serialized
        i.delete()


    def test_sharedTitles(self):
        i = Index().load({"title": "Parshanut Test"})
        if i:
            i.delete()
        schema = {
            "key": "Parshanut Test",
            "titles": [
                {
                    "lang": "en",
                    "text": "Parshanut Test",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגכג',
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Bereshit",
                    "sharedTitle": "Bereshit",
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Torah"]
                },
                {
                    "key": "Noach",
                    "sharedTitle": "Noach",
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Torah"]
                },
                {
                    "key": "Lech Lecha",
                    "sharedTitle": "Lech Lecha",
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Torah"]
                }
            ]
        }
        i = Index({
            "schema": schema,
            "title": "Parshanut Test",
            "categories": ["Chasidut"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        schema['titles'] = sorted(schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert schema == serialized
        i.delete()

    def test_alt_struct(self):
        i = Index().load({"title": "Stest"})
        if i:
            i.delete()
        schema = {
            "key": "Stest",
            "titles": [
                {
                    "lang": "en",
                    "text": "Stest",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגככג',
                    "primary": True
                }
            ],
            "nodeType": "JaggedArrayNode",
            "depth": 2,
            "addressTypes": ["Integer", "Integer"],
            "sectionNames": ["Chapter","Verse"]
        }

        structs = {
            "parasha": {
                "nodes": [
                    {
                        'sharedTitle': u'Shemot',
                        "nodeType": "ArrayMapNode",
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Aliyah"],
                        'wholeRef': u'Stest 1:1-6:1',
                        'refs': [
                                "Stest 1:1-1:17",
                                "Stest 1:18-2:10",
                                "Stest 2:11-2:25",
                                "Stest 3:1-3:15",
                                "Stest 3:16-4:17",
                                "Stest 4:18-4:31",
                                "Stest 5:1-6:1",
                        ]
                    },
                    {
                        'sharedTitle': u'Vaera',
                        "nodeType": "ArrayMapNode",
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Aliyah"],
                        'wholeRef': u'Stest 6:2-9:35',
                        'refs': [
                            "Stest 10:1-10:11",
                            "Stest 10:12-10:23",
                            "Stest 10:24-11:3",
                            "Stest 11:4-12:20",
                            "Stest 12:21-12:28",
                            "Stest 12:29-12:51",
                            "Stest 13:1-13:16",
                        ]
                    },
                ]
            }
        }

        creating_dict = {
            "schema": schema,
            "title": "Stest",
            "categories": ["Chasidut"],
            "alt_structs": structs
        }
        i = Index(creating_dict)
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        schema['titles'] = sorted(schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert schema == serialized

        contents =  i.contents(raw=True)
        contents['schema']['titles'] = sorted(contents['schema']['titles'], key=lambda x: x['text'])
        creating_dict['schema']['titles'] = sorted(creating_dict['schema']['titles'], key=lambda x: x['text'])
        assert contents == creating_dict

        assert Ref("Stest, Vaera 3") == Ref("Stest 10:24-11:3")
        assert Ref("Stest, Vaera") == Ref("Stest 6:2-9:35")
        i.delete()

    def test_numbered_primary_struct(self):
        i = Index().load({"title": "Stest"})
        if i:
            i.delete()
        schema = {
            "key": "Stest",
            "titles": [
                {
                    "lang": "en",
                    "text": "Stest",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגככג',
                    "primary": True
                }
            ],
            "nodeType": "JaggedArrayNode",
            "sectionNames": ["Parasha"],
            "addressTypes": ["Integer"],
            "depth": 1,
            "nodes": [
                {
                    "key": "s1",
                    'sharedTitle': u'Shemot',
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Vort"],
                },
                {
                    "key": "s2",
                    'sharedTitle': u'Vaera',
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Vort"],
                },
                {
                    "key": "s3",
                    'sharedTitle': u'Bo',
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Vort"],
                },
                {
                    "key": "s4",
                    'sharedTitle': u'Beshalach',
                    "nodeType": "JaggedArrayNode",
                    "depth": 1,
                    "addressTypes": ["Integer"],
                    "sectionNames": ["Vort"],
                },
            ]
        }

        creating_dict = {
            "schema": schema,
            "title": "Stest",
            "categories": ["Chasidut"],
        }
        i = Index(creating_dict)
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        schema['titles'] = sorted(schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert schema == serialized
        contents =  i.contents(raw=True)
        contents['schema']['titles'] = sorted(contents['schema']['titles'], key=lambda x: x['text'])
        creating_dict['schema']['titles'] = sorted(creating_dict['schema']['titles'], key=lambda x: x['text'])
        assert contents == creating_dict

        assert Ref("Stest 3:5") == Ref("Stest, Bo 5")
        assert Ref("Stest 3") == Ref("Stest, Bo")

        i.delete()

    def test_numbered_alt_struct(self):
        i = Index().load({"title": "Stest"})
        if i:
            i.delete()
        schema = {
            "key": "Stest",
            "titles": [
                {
                    "lang": "en",
                    "text": "Stest",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגככג',
                    "primary": True
                }
            ],
            "nodeType": "JaggedArrayNode",
            "depth": 2,
            "addressTypes": ["Integer", "Integer"],
            "sectionNames": ["Chapter", "Verse"]
        }

        structs = {
            "parasha": {
                "nodeType": "NumberedTitledTreeNode",
                "sectionNames": ["Chapter"],
                "addressTypes": ["Perek"],
                "depth": 1,
                "nodes": [
                    {
                        'sharedTitle': u'Shemot',
                        "nodeType": "ArrayMapNode",
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Aliyah"],
                        'wholeRef': u'Stest 1:1-6:1',
                        'refs': [
                                "Stest 1:1-1:17",
                                "Stest 1:18-2:10",
                                "Stest 2:11-2:25",
                                "Stest 3:1-3:15",
                                "Stest 3:16-4:17",
                                "Stest 4:18-4:31",
                                "Stest 5:1-6:1",
                        ]
                    },
                    {
                        'sharedTitle': u'Vaera',
                        "nodeType": "ArrayMapNode",
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Aliyah"],
                        'wholeRef': u'Stest 6:2-9:35',
                        'refs': [
                            "Stest 10:1-10:11",
                            "Stest 10:12-10:23",
                            "Stest 10:24-11:3",
                            "Stest 11:4-12:20",
                            "Stest 12:21-12:28",
                            "Stest 12:29-12:51",
                            "Stest 13:1-13:16",
                        ]
                    },
                ]
            }
        }

        creating_dict = {
            "schema": schema,
            "title": "Stest",
            "categories": ["Chasidut"],
            "alt_structs": structs
        }
        i = Index(creating_dict)
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        schema['titles'] = sorted(schema['titles'], key=lambda x: x['text'])
        serialized = i.nodes.serialize()
        serialized['titles'] = sorted(serialized['titles'], key=lambda x: x['text'])
        assert schema == serialized
        contents =  i.contents(raw=True)
        contents['schema']['titles'] = sorted(contents['schema']['titles'], key=lambda x: x['text'])
        creating_dict['schema']['titles'] = sorted(creating_dict['schema']['titles'], key=lambda x: x['text'])
        assert contents == creating_dict

        assert Ref("Stest Perek 2:3") == Ref("Stest, Vaera 3")
        assert Ref("Stest Perek 2:3") == Ref("Stest 10:24-11:3")

        i.delete()


#todo : test default
