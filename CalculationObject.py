class CalculationObject:
    def __init__(self, symbol, closingPrice, marketValue, indexShares, indexWeight, companyName, isin,
                 assetName, PartyNameInSCD, BloombergName, PostionOMXS30, TotalNumberOutstandingSharesPerIssuer,
                 OMX30Nominellt,
                 TotalOutstandsingSharesSCB=0, AvistaInnehav=0, TRSLongValue=0, TRSShortWeight='',
                 TRSShortValue=0):

        # Från NASDAQ filen
        self.symbol = symbol
        self.closingPrice = closingPrice
        self.marketValue = marketValue
        self.indexShares = indexShares
        self.indexWeight = indexWeight
        self.companyName = companyName
        self.isin = isin
        self.OMX30Nominellt = OMX30Nominellt

        # Från Statiska filen
        self.assetName = assetName
        self.PartyNameInSCD = PartyNameInSCD
        self.BloombergName = BloombergName.split(",")
        self.BloombergNameWithEquity = [s + ' Equity' for s in self.BloombergName]

        # Från Simcorp
        self.PostionOMXS30 = PostionOMXS30
        self.TotalOutstandsingSharesSCB = TotalOutstandsingSharesSCB
        self.AvistaInnehav = AvistaInnehav

        # Från UBS fil
        self.TRSLongValue = TRSLongValue

        # Från Pearl
        self.TRSShortWeight = TRSShortWeight
        self.TRSShortValue = TRSShortValue

    def as_dict(self):

        return {'Asset Name (Nasdaq)': self.symbol,
                'Closing Price (Nasdaq)': self.closingPrice,
                'Asset Name (Nasdaq)': self.assetName,
                'ISIN (Nasdaq)': self.isin,
                'Ticker manuellt justerad': listToString(self.BloombergName),
                'Total current number of shares outstanding SCD': self.TotalOutstandsingSharesSCB,
                'Vikt(%)': self.indexWeight,
                "Postion OMXS30": self.PostionOMXS30,
                "Position i bolag via OMX30": self.getPostionInCompany(),
                "Position i bolag via OMX30 Nominellt": self.OMX30Nominellt,
                "Avistainnehav Nominellt": self.AvistaInnehav,
                "Antal aktier - kort nettoposition": self.OMX30Nominellt + self.AvistaInnehav,

                # TRS
                "TRS Långa Värde Nominellt": self.TRSLongValue,
                "TRS Kort Vikt": self.getTRSShortWeight(),
                "TRS Korta Nominellt": self.TRSShortValue,
                "TRS Korta + Långa": self.TRSLongValue + self.TRSShortValue,
                "Totalt netto OMX, avista & TRS":

                    self.OMX30Nominellt +
                    self.AvistaInnehav +
                    self.TRSLongValue +
                    self.TRSShortValue
            ,
                "Postion att rapportera": round(self.getPositiontoReport(), 4),
                "Postion att rapportera i %": round(self.getPositiontoReport() * 100, 4)
                }

    def UpdateTotalOutstandsingSharesSCB(self, NewTotalOutstandsingSharesSCB):
        self.TotalOutstandsingSharesSCB = int(self.TotalOutstandsingSharesSCB) + NewTotalOutstandsingSharesSCB

    def UpdateAvistaInnehav(self, NewAvistaInnehav):
        self.AvistaInnehav = NewAvistaInnehav

    def UpdateTRSLongValue(self, NewTRSLongValue):
        self.TRSLongValue = self.TRSLongValue + NewTRSLongValue

    def UpdateTRSShortWeight(self, NewTRSShortWeight):
        self.TRSShortWeight = self.TRSShortWeight + ', ' + str(NewTRSShortWeight)

    def UpdateTRSShortValue(self, NewTRSShortValue):
        self.TRSShortValue = self.TRSShortValue + NewTRSShortValue

    def getTRSShortWeight(self):
        if self.TRSShortWeight == '':
            return '0'
        else:
            return self.TRSShortWeight[2:]

    def getPostionInCompany(self):
        return (self.indexWeight * self.PostionOMXS30) / 100

    def getPositiontoReport(self):
        return (((self.OMX30Nominellt + self.AvistaInnehav + self.TRSLongValue +
                  (self.TRSShortValue)) / self.TotalOutstandsingSharesSCB)