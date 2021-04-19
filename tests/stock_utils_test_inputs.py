"""
INPUTS and EXPECTED OUTPUTS FOR STOCK_UTILS_TEST.PY
"""

INPUT1 = [{
    'Mega': {
        'MSFT': {
            'Symbol': 'MSFT',
            'Company': 'Microsoft Corporation',
            'High': None,
            'Low': None,
            'Price': 269.32,
            'Category': 'Mega'
        },
        'V': {
            'Symbol': 'V',
            'Company': 'Visa Inc - Class A',
            'High': None,
            'Low': None,
            'Price': 234.46,
            'Category': 'Mega'
        },
        'GOOGL': {
            'Symbol': 'GOOGL',
            'Company': 'Alphabet Inc - Class A',
            'High': None,
            'Low': None,
            'Price': 2387.7,
            'Category': 'Mega'
        },
        'BAC': {
            'Symbol': 'BAC',
            'Company': 'Bank Of America Corp.',
            'High': None,
            'Low': None,
            'Price': 40.92,
            'Category': 'Mega'
        }
    }
}, {
    'Tech': {
        'CRM': {
            'Symbol': 'CRM',
            'Company': 'Salesforce.Com Inc',
            'High': None,
            'Low': None,
            'Price': 236.61,
            'Category': 'Tech'
        },
        'GOOGL': {
            'Symbol': 'GOOGL',
            'Company': 'Alphabet Inc - Class A',
            'High': None,
            'Low': None,
            'Price': 2356.5,
            'Category': 'Tech'
        },
        'MSFT': {
            'Symbol': 'MSFT',
            'Company': 'Microsoft Corporation',
            'High': None,
            'Low': None,
            'Price': 261.3,
            'Category': 'Tech'
        },
        'CSCO': {
            'Symbol': 'CSCO',
            'Company': 'Cisco Systems, Inc.',
            'High': None,
            'Low': None,
            'Price': 53.42,
            'Category': 'Tech'
        }
    }
}, {
    'Energy': {
        'PBR': {
            'Symbol': 'PBR',
            'Company': 'Petroleo Brasileiro S.A. Petrobras - ADR',
            'High': None,
            'Low': None,
            'Price': 8.52,
            'Category': 'Energy'
        },
        'MPC': {
            'Symbol': 'MPC',
            'Company': 'Marathon Petroleum Corp',
            'High': None,
            'Low': None,
            'Price': 55.7,
            'Category': 'Energy'
        },
        'PTR': {
            'Symbol': 'PTR',
            'Company': 'PetroChina Co. Ltd. - ADR',
            'High': None,
            'Low': None,
            'Price': 37.86,
            'Category': 'Energy'
        },
        'CMI': {
            'Symbol': 'CMI',
            'Company': 'Cummins Inc.',
            'High': None,
            'Low': None,
            'Price': 273.03,
            'Category': 'Energy'
        }
    }
}, {
    'Utilities': {
        'TU': {
            'Symbol': 'TU',
            'Company': 'Telus Corp.',
            'High': None,
            'Low': None,
            'Price': 21.47,
            'Category': 'Utilities'
        },
        'AEE': {
            'Symbol': 'AEE',
            'Company': 'Ameren Corp.',
            'High': None,
            'Low': None,
            'Price': 84.26,
            'Category': 'Utilities'
        },
        'D': {
            'Symbol': 'D',
            'Company': 'Dominion Energy Inc',
            'High': None,
            'Low': None,
            'Price': 82.56,
            'Category': 'Utilities'
        },
        'T': {
            'Symbol': 'T',
            'Company': 'AT&T, Inc.',
            'High': None,
            'Low': None,
            'Price': 31.32,
            'Category': 'Utilities'
        }
    }
}, {
    'Finance': {
        'MS': {
            'Symbol': 'MS',
            'Company': 'Morgan Stanley',
            'High': None,
            'Low': None,
            'Price': 80.06,
            'Category': 'Finance'
        },
        'USB': {
            'Symbol': 'USB',
            'Company': 'U.S. Bancorp.',
            'High': None,
            'Low': None,
            'Price': 59.96,
            'Category': 'Finance'
        },
        'MKTX': {
            'Symbol': 'MKTX',
            'Company': 'MarketAxess Holdings Inc.',
            'High': None,
            'Low': None,
            'Price': 560.07,
            'Category': 'Finance'
        },
        'AJG': {
            'Symbol': 'AJG',
            'Company': 'Arthur J. Gallagher & Co.',
            'High': None,
            'Low': None,
            'Price': 142,
            'Category': 'Finance'
        }
    }
}]
INPUT2 = [{
    'Mega': {
        'JPM': {
            'Symbol': 'JPM',
            'Company': 'JPMorgan Chase & Co.',
            'High': None,
            'Low': None,
            'Price': 158.5,
            'Category': 'Mega'
        },
        'CMCSA': {
            'Symbol': 'CMCSA',
            'Company': 'Comcast Corp - Class A',
            'High': None,
            'Low': None,
            'Price': 56.63,
            'Category': 'Mega'
        },
        'ADBE': {
            'Symbol': 'ADBE',
            'Company': 'Adobe Inc',
            'High': None,
            'Low': None,
            'Price': 547.04,
            'Category': 'Mega'
        },
        'CVX': {
            'Symbol': 'CVX',
            'Company': 'Chevron Corp.',
            'High': None,
            'Low': None,
            'Price': 107.59,
            'Category': 'Mega'
        }
    }
}, {
    'Tech': {
        'CSCO': {
            'Symbol': 'CSCO',
            'Company': 'Cisco Systems, Inc.',
            'High': None,
            'Low': None,
            'Price': 54.366,
            'Category': 'Tech'
        },
        'GOOG': {
            'Symbol': 'GOOG',
            'Company': 'Alphabet Inc - Class C',
            'High': None,
            'Low': None,
            'Price': 2405.83,
            'Category': 'Tech'
        },
        'ADBE': {
            'Symbol': 'ADBE',
            'Company': 'Adobe Inc',
            'High': None,
            'Low': None,
            'Price': 526.63,
            'Category': 'Tech'
        },
        'ORCL': {
            'Symbol': 'ORCL',
            'Company': 'Oracle Corp.',
            'High': None,
            'Low': None,
            'Price': 81.24,
            'Category': 'Tech'
        }
    }
}, {
    'Energy': {
        'VLO': {
            'Symbol': 'VLO',
            'Company': 'Valero Energy Corp.',
            'High': None,
            'Low': None,
            'Price': 74.8,
            'Category': 'Energy'
        },
        'IMO': {
            'Symbol': 'IMO',
            'Company': 'Imperial Oil Ltd.',
            'High': None,
            'Low': None,
            'Price': 26,
            'Category': 'Energy'
        },
        'XOM': {
            'Symbol': 'XOM',
            'Company': 'Exxon Mobil Corp.',
            'High': None,
            'Low': None,
            'Price': 57.68,
            'Category': 'Energy'
        },
        'MPLX': {
            'Symbol': 'MPLX',
            'Company': 'MPLX LP - Unit',
            'High': None,
            'Low': None,
            'Price': 27.65,
            'Category': 'Energy'
        }
    }
}, {
    'Utilities': {
        'OKE': {
            'Symbol': 'OKE',
            'Company': 'Oneok Inc.',
            'High': None,
            'Low': None,
            'Price': 51.8,
            'Category': 'Utilities'
        },
        'AMX': {
            'Symbol': 'AMX',
            'Company': 'America Movil S.A.B.DE C.V. - ADR - Series L',
            'High': None,
            'Low': None,
            'Price': 15.05,
            'Category': 'Utilities'
        },
        'EPD': {
            'Symbol': 'EPD',
            'Company': 'Enterprise Products Partners L P - Unit',
            'High': None,
            'Low': None,
            'Price': 23.93,
            'Category': 'Utilities'
        },
        'CQP': {
            'Symbol': 'CQP',
            'Company': 'Cheniere Energy Partners LP - Unit',
            'High': None,
            'Low': None,
            'Price': 43.19,
            'Category': 'Utilities'
        }
    }
}, {
    'Finance': {
        'AON': {
            'Symbol': 'AON',
            'Company': 'Aon plc. - Class A',
            'High': None,
            'Low': None,
            'Price': 246.33,
            'Category': 'Finance'
        },
        'RY': {
            'Symbol': 'RY',
            'Company': 'Royal Bank Of Canada',
            'High': None,
            'Low': None,
            'Price': 96.54,
            'Category': 'Finance'
        },
        'OPEN': {
            'Symbol': 'OPEN',
            'Company': 'Opendoor Technologies Inc',
            'High': None,
            'Low': None,
            'Price': 18.51,
            'Category': 'Finance'
        },
        'CNA': {
            'Symbol': 'CNA',
            'Company': 'CNA Financial Corp.',
            'High': None,
            'Low': None,
            'Price': 48.57,
            'Category': 'Finance'
        }
    }
}]
INPUT3 = [{
    'Mega': {
        'PYPL': {
            'Symbol': 'PYPL',
            'Company': 'PayPal Holdings Inc',
            'High': None,
            'Low': None,
            'Price': 281.67,
            'Category': 'Mega'
        },
        'VZ': {
            'Symbol': 'VZ',
            'Company': 'Verizon Communications Inc',
            'High': None,
            'Low': None,
            'Price': 58.89,
            'Category': 'Mega'
        },
        'UNH': {
            'Symbol': 'UNH',
            'Company': 'Unitedhealth Group Inc',
            'High': None,
            'Low': None,
            'Price': 392.49,
            'Category': 'Mega'
        },
        'BAC': {
            'Symbol': 'BAC',
            'Company': 'Bank Of America Corp.',
            'High': None,
            'Low': None,
            'Price': 40.3,
            'Category': 'Mega'
        }
    }
}, {
    'Tech': {
        'GOOGL': {
            'Symbol': 'GOOGL',
            'Company': 'Alphabet Inc - Class A',
            'High': None,
            'Low': None,
            'Price': 2376.93,
            'Category': 'Tech'
        },
        'INTC': {
            'Symbol': 'INTC',
            'Company': 'Intel Corp.',
            'High': None,
            'Low': None,
            'Price': 65.11,
            'Category': 'Tech'
        },
        'ADBE': {
            'Symbol': 'ADBE',
            'Company': 'Adobe Inc',
            'High': None,
            'Low': None,
            'Price': 537.43,
            'Category': 'Tech'
        },
        'ORCL': {
            'Symbol': 'ORCL',
            'Company': 'Oracle Corp.',
            'High': None,
            'Low': None,
            'Price': 80.2,
            'Category': 'Tech'
        }
    }
}, {
    'Energy': {
        'IMO': {
            'Symbol': 'IMO',
            'Company': 'Imperial Oil Ltd.',
            'High': None,
            'Low': None,
            'Price': 26.26,
            'Category': 'Energy'
        },
        'MPLX': {
            'Symbol': 'MPLX',
            'Company': 'MPLX LP - Unit',
            'High': None,
            'Low': None,
            'Price': 27.02,
            'Category': 'Energy'
        },
        'E': {
            'Symbol': 'E',
            'Company': 'Eni Spa - ADR',
            'High': None,
            'Low': None,
            'Price': 24.97,
            'Category': 'Energy'
        },
        'HES': {
            'Symbol': 'HES',
            'Company': 'Hess Corporation',
            'High': None,
            'Low': None,
            'Price': 72.04,
            'Category': 'Energy'
        }
    }
}, {
    'Utilities': {
        'T': {
            'Symbol': 'T',
            'Company': 'AT&T, Inc.',
            'High': None,
            'Low': None,
            'Price': 30.52,
            'Category': 'Utilities'
        },
        'D': {
            'Symbol': 'D',
            'Company': 'Dominion Energy Inc',
            'High': None,
            'Low': None,
            'Price': 82.35,
            'Category': 'Utilities'
        },
        'AMOV': {
            'Symbol': 'AMOV',
            'Company': 'America Movil S.A.B.DE C.V. - ADR - Class A',
            'High': None,
            'Low': None,
            'Price': 14.48,
            'Category': 'Utilities'
        },
        'AEE': {
            'Symbol': 'AEE',
            'Company': 'Ameren Corp.',
            'High': None,
            'Low': None,
            'Price': 87.24,
            'Category': 'Utilities'
        }
    }
}, {
    'Finance': {
        'NTRS': {
            'Symbol': 'NTRS',
            'Company': 'Northern Trust Corp.',
            'High': None,
            'Low': None,
            'Price': 109.596,
            'Category': 'Finance'
        },
        'GL': {
            'Symbol': 'GL',
            'Company': 'Globe Life Inc',
            'High': None,
            'Low': None,
            'Price': 106.1,
            'Category': 'Finance'
        },
        'AXP': {
            'Symbol': 'AXP',
            'Company': 'American Express Co.',
            'High': None,
            'Low': None,
            'Price': 150.91,
            'Category': 'Finance'
        },
        'TFC': {
            'Symbol': 'TFC',
            'Company': 'Truist Financial Corporation',
            'High': None,
            'Low': None,
            'Price': 59.22,
            'Category': 'Finance'
        }
    }
}]

EXPECTED1 = {
    'allStocks': [{
        'Symbol': 'MSFT',
        'Company': 'Microsoft Corporation',
        'High': None,
        'Low': None,
        'Price': 269.32,
        'Category': 'Mega'
    }, {
        'Symbol': 'V',
        'Company': 'Visa Inc - Class A',
        'High': None,
        'Low': None,
        'Price': 234.46,
        'Category': 'Mega'
    }, {
        'Symbol': 'GOOGL',
        'Company': 'Alphabet Inc - Class A',
        'High': None,
        'Low': None,
        'Price': 2387.7,
        'Category': 'Mega'
    }, {
        'Symbol': 'BAC',
        'Company': 'Bank Of America Corp.',
        'High': None,
        'Low': None,
        'Price': 40.92,
        'Category': 'Mega'
    }, {
        'Symbol': 'CRM',
        'Company': 'Salesforce.Com Inc',
        'High': None,
        'Low': None,
        'Price': 236.61,
        'Category': 'Tech'
    }, {
        'Symbol': 'GOOGL',
        'Company': 'Alphabet Inc - Class A',
        'High': None,
        'Low': None,
        'Price': 2356.5,
        'Category': 'Tech'
    }, {
        'Symbol': 'MSFT',
        'Company': 'Microsoft Corporation',
        'High': None,
        'Low': None,
        'Price': 261.3,
        'Category': 'Tech'
    }, {
        'Symbol': 'CSCO',
        'Company': 'Cisco Systems, Inc.',
        'High': None,
        'Low': None,
        'Price': 53.42,
        'Category': 'Tech'
    }, {
        'Symbol': 'PBR',
        'Company': 'Petroleo Brasileiro S.A. Petrobras - ADR',
        'High': None,
        'Low': None,
        'Price': 8.52,
        'Category': 'Energy'
    }, {
        'Symbol': 'MPC',
        'Company': 'Marathon Petroleum Corp',
        'High': None,
        'Low': None,
        'Price': 55.7,
        'Category': 'Energy'
    }, {
        'Symbol': 'PTR',
        'Company': 'PetroChina Co. Ltd. - ADR',
        'High': None,
        'Low': None,
        'Price': 37.86,
        'Category': 'Energy'
    }, {
        'Symbol': 'CMI',
        'Company': 'Cummins Inc.',
        'High': None,
        'Low': None,
        'Price': 273.03,
        'Category': 'Energy'
    }, {
        'Symbol': 'TU',
        'Company': 'Telus Corp.',
        'High': None,
        'Low': None,
        'Price': 21.47,
        'Category': 'Utilities'
    }, {
        'Symbol': 'AEE',
        'Company': 'Ameren Corp.',
        'High': None,
        'Low': None,
        'Price': 84.26,
        'Category': 'Utilities'
    }, {
        'Symbol': 'D',
        'Company': 'Dominion Energy Inc',
        'High': None,
        'Low': None,
        'Price': 82.56,
        'Category': 'Utilities'
    }, {
        'Symbol': 'T',
        'Company': 'AT&T, Inc.',
        'High': None,
        'Low': None,
        'Price': 31.32,
        'Category': 'Utilities'
    }, {
        'Symbol': 'MS',
        'Company': 'Morgan Stanley',
        'High': None,
        'Low': None,
        'Price': 80.06,
        'Category': 'Finance'
    }, {
        'Symbol': 'USB',
        'Company': 'U.S. Bancorp.',
        'High': None,
        'Low': None,
        'Price': 59.96,
        'Category': 'Finance'
    }, {
        'Symbol': 'MKTX',
        'Company': 'MarketAxess Holdings Inc.',
        'High': None,
        'Low': None,
        'Price': 560.07,
        'Category': 'Finance'
    }, {
        'Symbol': 'AJG',
        'Company': 'Arthur J. Gallagher & Co.',
        'High': None,
        'Low': None,
        'Price': 142,
        'Category': 'Finance'
    }]
}
EXPECTED2 = {
    'allStocks': [{
        'Symbol': 'JPM',
        'Company': 'JPMorgan Chase & Co.',
        'High': None,
        'Low': None,
        'Price': 158.5,
        'Category': 'Mega'
    }, {
        'Symbol': 'CMCSA',
        'Company': 'Comcast Corp - Class A',
        'High': None,
        'Low': None,
        'Price': 56.63,
        'Category': 'Mega'
    }, {
        'Symbol': 'ADBE',
        'Company': 'Adobe Inc',
        'High': None,
        'Low': None,
        'Price': 547.04,
        'Category': 'Mega'
    }, {
        'Symbol': 'CVX',
        'Company': 'Chevron Corp.',
        'High': None,
        'Low': None,
        'Price': 107.59,
        'Category': 'Mega'
    }, {
        'Symbol': 'CSCO',
        'Company': 'Cisco Systems, Inc.',
        'High': None,
        'Low': None,
        'Price': 54.366,
        'Category': 'Tech'
    }, {
        'Symbol': 'GOOG',
        'Company': 'Alphabet Inc - Class C',
        'High': None,
        'Low': None,
        'Price': 2405.83,
        'Category': 'Tech'
    }, {
        'Symbol': 'ADBE',
        'Company': 'Adobe Inc',
        'High': None,
        'Low': None,
        'Price': 526.63,
        'Category': 'Tech'
    }, {
        'Symbol': 'ORCL',
        'Company': 'Oracle Corp.',
        'High': None,
        'Low': None,
        'Price': 81.24,
        'Category': 'Tech'
    }, {
        'Symbol': 'VLO',
        'Company': 'Valero Energy Corp.',
        'High': None,
        'Low': None,
        'Price': 74.8,
        'Category': 'Energy'
    }, {
        'Symbol': 'IMO',
        'Company': 'Imperial Oil Ltd.',
        'High': None,
        'Low': None,
        'Price': 26,
        'Category': 'Energy'
    }, {
        'Symbol': 'XOM',
        'Company': 'Exxon Mobil Corp.',
        'High': None,
        'Low': None,
        'Price': 57.68,
        'Category': 'Energy'
    }, {
        'Symbol': 'MPLX',
        'Company': 'MPLX LP - Unit',
        'High': None,
        'Low': None,
        'Price': 27.65,
        'Category': 'Energy'
    }, {
        'Symbol': 'OKE',
        'Company': 'Oneok Inc.',
        'High': None,
        'Low': None,
        'Price': 51.8,
        'Category': 'Utilities'
    }, {
        'Symbol': 'AMX',
        'Company': 'America Movil S.A.B.DE C.V. - ADR - Series L',
        'High': None,
        'Low': None,
        'Price': 15.05,
        'Category': 'Utilities'
    }, {
        'Symbol': 'EPD',
        'Company': 'Enterprise Products Partners L P - Unit',
        'High': None,
        'Low': None,
        'Price': 23.93,
        'Category': 'Utilities'
    }, {
        'Symbol': 'CQP',
        'Company': 'Cheniere Energy Partners LP - Unit',
        'High': None,
        'Low': None,
        'Price': 43.19,
        'Category': 'Utilities'
    }, {
        'Symbol': 'AON',
        'Company': 'Aon plc. - Class A',
        'High': None,
        'Low': None,
        'Price': 246.33,
        'Category': 'Finance'
    }, {
        'Symbol': 'RY',
        'Company': 'Royal Bank Of Canada',
        'High': None,
        'Low': None,
        'Price': 96.54,
        'Category': 'Finance'
    }, {
        'Symbol': 'OPEN',
        'Company': 'Opendoor Technologies Inc',
        'High': None,
        'Low': None,
        'Price': 18.51,
        'Category': 'Finance'
    }, {
        'Symbol': 'CNA',
        'Company': 'CNA Financial Corp.',
        'High': None,
        'Low': None,
        'Price': 48.57,
        'Category': 'Finance'
    }]
}
EXPECTED3 = {
    'allStocks': [{
        'Symbol': 'PYPL',
        'Company': 'PayPal Holdings Inc',
        'High': None,
        'Low': None,
        'Price': 281.67,
        'Category': 'Mega'
    }, {
        'Symbol': 'VZ',
        'Company': 'Verizon Communications Inc',
        'High': None,
        'Low': None,
        'Price': 58.89,
        'Category': 'Mega'
    }, {
        'Symbol': 'UNH',
        'Company': 'Unitedhealth Group Inc',
        'High': None,
        'Low': None,
        'Price': 392.49,
        'Category': 'Mega'
    }, {
        'Symbol': 'BAC',
        'Company': 'Bank Of America Corp.',
        'High': None,
        'Low': None,
        'Price': 40.3,
        'Category': 'Mega'
    }, {
        'Symbol': 'GOOGL',
        'Company': 'Alphabet Inc - Class A',
        'High': None,
        'Low': None,
        'Price': 2376.93,
        'Category': 'Tech'
    }, {
        'Symbol': 'INTC',
        'Company': 'Intel Corp.',
        'High': None,
        'Low': None,
        'Price': 65.11,
        'Category': 'Tech'
    }, {
        'Symbol': 'ADBE',
        'Company': 'Adobe Inc',
        'High': None,
        'Low': None,
        'Price': 537.43,
        'Category': 'Tech'
    }, {
        'Symbol': 'ORCL',
        'Company': 'Oracle Corp.',
        'High': None,
        'Low': None,
        'Price': 80.2,
        'Category': 'Tech'
    }, {
        'Symbol': 'IMO',
        'Company': 'Imperial Oil Ltd.',
        'High': None,
        'Low': None,
        'Price': 26.26,
        'Category': 'Energy'
    }, {
        'Symbol': 'MPLX',
        'Company': 'MPLX LP - Unit',
        'High': None,
        'Low': None,
        'Price': 27.02,
        'Category': 'Energy'
    }, {
        'Symbol': 'E',
        'Company': 'Eni Spa - ADR',
        'High': None,
        'Low': None,
        'Price': 24.97,
        'Category': 'Energy'
    }, {
        'Symbol': 'HES',
        'Company': 'Hess Corporation',
        'High': None,
        'Low': None,
        'Price': 72.04,
        'Category': 'Energy'
    }, {
        'Symbol': 'T',
        'Company': 'AT&T, Inc.',
        'High': None,
        'Low': None,
        'Price': 30.52,
        'Category': 'Utilities'
    }, {
        'Symbol': 'D',
        'Company': 'Dominion Energy Inc',
        'High': None,
        'Low': None,
        'Price': 82.35,
        'Category': 'Utilities'
    }, {
        'Symbol': 'AMOV',
        'Company': 'America Movil S.A.B.DE C.V. - ADR - Class A',
        'High': None,
        'Low': None,
        'Price': 14.48,
        'Category': 'Utilities'
    }, {
        'Symbol': 'AEE',
        'Company': 'Ameren Corp.',
        'High': None,
        'Low': None,
        'Price': 87.24,
        'Category': 'Utilities'
    }, {
        'Symbol': 'NTRS',
        'Company': 'Northern Trust Corp.',
        'High': None,
        'Low': None,
        'Price': 109.596,
        'Category': 'Finance'
    }, {
        'Symbol': 'GL',
        'Company': 'Globe Life Inc',
        'High': None,
        'Low': None,
        'Price': 106.1,
        'Category': 'Finance'
    }, {
        'Symbol': 'AXP',
        'Company': 'American Express Co.',
        'High': None,
        'Low': None,
        'Price': 150.91,
        'Category': 'Finance'
    }, {
        'Symbol': 'TFC',
        'Company': 'Truist Financial Corporation',
        'High': None,
        'Low': None,
        'Price': 59.22,
        'Category': 'Finance'
    }]
}
