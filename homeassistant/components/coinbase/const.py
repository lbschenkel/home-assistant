"""Constants used for Coinbase."""

CONF_CURRENCIES = "account_balance_currencies"
CONF_EXCHANGE_RATES = "exchange_rate_currencies"
CONF_OPTIONS = "options"
DOMAIN = "coinbase"

# These are constants used by the previous YAML configuration
CONF_YAML_API_TOKEN = "api_secret"

# Constants for data returned by Coinbase API
API_ACCOUNT_AMOUNT = "amount"
API_ACCOUNT_BALANCE = "balance"
API_ACCOUNT_CURRENCY = "currency"
API_ACCOUNT_ID = "id"
API_ACCOUNT_NATIVE_BALANCE = "native_balance"
API_ACCOUNT_NAME = "name"
API_ACCOUNTS_DATA = "data"
API_RATES = "rates"

WALLETS = {
    "AAVE": "AAVE",
    "ALGO": "ALGO",
    "ATOM": "ATOM",
    "BAL": "BAL",
    "BAND": "BAND",
    "BAT": "BAT",
    "BCH": "BCH",
    "BNT": "BNT",
    "BSV": "BSV",
    "BTC": "BTC",
    "CGLD": "CLGD",
    "CVC": "CVC",
    "COMP": "COMP",
    "DAI": "DAI",
    "DNT": "DNT",
    "EOS": "EOS",
    "ETC": "ETC",
    "ETH": "ETH",
    "EUR": "EUR",
    "FIL": "FIL",
    "GBP": "GBP",
    "GRT": "GRT",
    "KNC": "KNC",
    "LINK": "LINK",
    "LRC": "LRC",
    "LTC": "LTC",
    "MANA": "MANA",
    "MKR": "MKR",
    "NMR": "NMR",
    "NU": "NU",
    "OMG": "OMG",
    "OXT": "OXT",
    "REP": "REP",
    "REPV2": "REPV2",
    "SNX": "SNX",
    "UMA": "UMA",
    "UNI": "UNI",
    "USDC": "USDC",
    "WBTC": "WBTC",
    "XLM": "XLM",
    "XRP": "XRP",
    "XTZ": "XTZ",
    "YFI": "YFI",
    "ZRX": "ZRX",
}

RATES = {
    "1INCH": "1INCH",
    "AAVE": "AAVE",
    "ADA": "ADA",
    "AED": "AED",
    "AFN": "AFN",
    "ALGO": "ALGO",
    "ALL": "ALL",
    "AMD": "AMD",
    "ANG": "ANG",
    "ANKR": "ANKR",
    "AOA": "AOA",
    "ARS": "ARS",
    "ATOM": "ATOM",
    "AUD": "AUD",
    "AWG": "AWG",
    "AZN": "AZN",
    "BAL": "BAL",
    "BAM": "BAM",
    "BAND": "BAND",
    "BAT": "BAT",
    "BBD": "BBD",
    "BCH": "BCH",
    "BDT": "BDT",
    "BGN": "BGN",
    "BHD": "BHD",
    "BIF": "BIF",
    "BMD": "BMD",
    "BND": "BND",
    "BNT": "BNT",
    "BOB": "BOB",
    "BRL": "BRL",
    "BSD": "BSD",
    "BSV": "BSV",
    "BTC": "BTC",
    "BTN": "BTN",
    "BWP": "BWP",
    "BYN": "BYN",
    "BYR": "BYR",
    "BZD": "BZD",
    "CAD": "CAD",
    "CDF": "CDF",
    "CGLD": "CGLD",
    "CHF": "CHF",
    "CLF": "CLF",
    "CLP": "CLP",
    "CNH": "CNH",
    "CNY": "CNY",
    "COMP": "COMP",
    "COP": "COP",
    "CRC": "CRC",
    "CRV": "CRV",
    "CUC": "CUC",
    "CVC": "CVC",
    "CVE": "CVE",
    "CZK": "CZK",
    "DAI": "DAI",
    "DASH": "DASH",
    "DJF": "DJF",
    "DKK": "DKK",
    "DNT": "DNT",
    "DOP": "DOP",
    "DZD": "DZD",
    "EGP": "EGP",
    "ENJ": "ENJ",
    "EOS": "EOS",
    "ERN": "ERN",
    "ETB": "ETB",
    "ETC": "ETC",
    "ETH": "ETH",
    "ETH2": "ETH2",
    "EUR": "EUR",
    "FIL": "FIL",
    "FJD": "FJD",
    "FKP": "FKP",
    "FORTH": "FORTH",
    "GBP": "GBP",
    "GBX": "GBX",
    "GEL": "GEL",
    "GGP": "GGP",
    "GHS": "GHS",
    "GIP": "GIP",
    "GMD": "GMD",
    "GNF": "GNF",
    "GRT": "GRT",
    "GTQ": "GTQ",
    "GYD": "GYD",
    "HKD": "HKD",
    "HNL": "HNL",
    "HRK": "HRK",
    "HTG": "HTG",
    "HUF": "HUF",
    "IDR": "IDR",
    "ILS": "ILS",
    "IMP": "IMP",
    "INR": "INR",
    "IQD": "IQD",
    "ISK": "ISK",
    "JEP": "JEP",
    "JMD": "JMD",
    "JOD": "JOD",
    "JPY": "JPY",
    "KES": "KES",
    "KGS": "KGS",
    "KHR": "KHR",
    "KMF": "KMF",
    "KNC": "KNC",
    "KRW": "KRW",
    "KWD": "KWD",
    "KYD": "KYD",
    "KZT": "KZT",
    "LAK": "LAK",
    "LBP": "LBP",
    "LINK": "LINK",
    "LKR": "LKR",
    "LRC": "LRC",
    "LRD": "LRD",
    "LSL": "LSL",
    "LTC": "LTC",
    "LYD": "LYD",
    "MAD": "MAD",
    "MANA": "MANA",
    "MATIC": "MATIC",
    "MDL": "MDL",
    "MGA": "MGA",
    "MKD": "MKD",
    "MKR": "MKR",
    "MMK": "MMK",
    "MNT": "MNT",
    "MOP": "MOP",
    "MRO": "MRO",
    "MTL": "MTL",
    "MUR": "MUR",
    "MVR": "MVR",
    "MWK": "MWK",
    "MXN": "MXN",
    "MYR": "MYR",
    "MZN": "MZN",
    "NAD": "NAD",
    "NGN": "NGN",
    "NIO": "NIO",
    "NKN": "NKN",
    "NMR": "NMR",
    "NOK": "NOK",
    "NPR": "NPR",
    "NU": "NU",
    "NZD": "NZD",
    "OGN": "OGN",
    "OMG": "OMG",
    "OMR": "OMR",
    "OXT": "OXT",
    "PAB": "PAB",
    "PEN": "PEN",
    "PGK": "PGK",
    "PHP": "PHP",
    "PKR": "PKR",
    "PLN": "PLN",
    "PYG": "PYG",
    "QAR": "QAR",
    "REN": "REN",
    "REP": "REP",
    "RON": "RON",
    "RSD": "RSD",
    "RUB": "RUB",
    "RWF": "RWF",
    "SAR": "SAR",
    "SBD": "SBD",
    "SCR": "SCR",
    "SEK": "SEK",
    "SGD": "SGD",
    "SHP": "SHP",
    "SKL": "SKL",
    "SLL": "SLL",
    "SNX": "SNX",
    "SOS": "SOS",
    "SRD": "SRD",
    "SSP": "SSP",
    "STD": "STD",
    "STORJ": "STORJ",
    "SUSHI": "SUSHI",
    "SVC": "SVC",
    "SZL": "SZL",
    "THB": "THB",
    "TJS": "TJS",
    "TMT": "TMT",
    "TND": "TND",
    "TOP": "TOP",
    "TRY": "TRY",
    "TTD": "TTD",
    "TWD": "TWD",
    "TZS": "TZS",
    "UAH": "UAH",
    "UGX": "UGX",
    "UMA": "UMA",
    "UNI": "UNI",
    "USD": "USD",
    "USDC": "USDC",
    "UYU": "UYU",
    "UZS": "UZS",
    "VES": "VES",
    "VND": "VND",
    "VUV": "VUV",
    "WBTC": "WBTC",
    "WST": "WST",
    "XAF": "XAF",
    "XAG": "XAG",
    "XAU": "XAU",
    "XCD": "XCD",
    "XDR": "XDR",
    "XLM": "XLM",
    "XOF": "XOF",
    "XPD": "XPD",
    "XPF": "XPF",
    "XPT": "XPT",
    "XTZ": "XTZ",
    "YER": "YER",
    "YFI": "YFI",
    "ZAR": "ZAR",
    "ZEC": "ZEC",
    "ZMW": "ZMW",
    "ZRX": "ZRX",
    "ZWL": "ZWL",
}
