from enum import Enum

from hitbtc.symbol.symbol import Symbol


class CurrencyPair(Enum):
    """
    Get list of avialable Symbols (Currency Pairs). You can read more info at
    http://www.investopedia.com/terms/c/currencypair.asp
    """

    BCN_BTC = Symbol(id="BCNBTC")
    BTC_USD = Symbol(id="BTCUSD")
    DASH_BTC = Symbol(id="DASHBTC")
    DOGE_BTC = Symbol(id="DOGEBTC")
    DOGE_USD = Symbol(id="DOGEUSD")
    EMC_BTC = Symbol(id="EMCBTC")
    ETH_BTC: Symbol = Symbol(id="ETHBTC")
    LSK_BTC = Symbol(id="LSKBTC")
    LTC_BTC = Symbol(id="LTCBTC")
    LTC_USD = Symbol(id="LTCUSD")
    NXT_BTC = Symbol(id="NXTBTC")
    SBD_BTC = Symbol(id="SBDBTC")
    SC_BTC = Symbol(id="SCBTC")
    STEEM_BTC = Symbol(id="STEEMBTC")
    XDN_BTC = Symbol(id="XDNBTC")
    XEM_BTC = Symbol(id="XEMBTC")
    XMR_BTC = Symbol(id="XMRBTC")
    ARDR_BTC = Symbol(id="ARDRBTC")
    ZEC_BTC = Symbol(id="ZECBTC")
    WAVES_BTC = Symbol(id="WAVESBTC")
    MAID_BTC = Symbol(id="MAIDBTC")
    AMP_BTC = Symbol(id="AMPBTC")
    DGD_BTC = Symbol(id="DGDBTC")
    SNGLS_BTC = Symbol(id="SNGLSBTC")
    TRST_BTC = Symbol(id="TRSTBTC")
    TIME_BTC = Symbol(id="TIMEBTC")
    GNO_BTC = Symbol(id="GNOBTC")
    REP_BTC = Symbol(id="REPBTC")
    XMR_USD = Symbol(id="XMRUSD")
    DASH_USD = Symbol(id="DASHUSD")
    ETH_USD = Symbol(id="ETHUSD")
    NXT_USD = Symbol(id="NXTUSD")
    ZRC_BTC = Symbol(id="ZRCBTC")
    BOS_BTC = Symbol(id="BOSBTC")
    DCT_BTC = Symbol(id="DCTBTC")
    ANT_BTC = Symbol(id="ANTBTC")
    AEON_BTC = Symbol(id="AEONBTC")
    GUP_BTC = Symbol(id="GUPBTC")
    PLU_BTC = Symbol(id="PLUBTC")
    LUN_BTC = Symbol(id="LUNBTC")
    NXC_BTC = Symbol(id="NXCBTC")
    EDG_BTC = Symbol(id="EDGBTC")
    RLC_BTC = Symbol(id="RLCBTC")
    SWT_BTC = Symbol(id="SWTBTC")
    TKN_BTC = Symbol(id="TKNBTC")
    WINGS_BTC = Symbol(id="WINGSBTC")
    XAUR_BTC = Symbol(id="XAURBTC")
    AE_BTC = Symbol(id="AEBTC")
    PTOY_BTC = Symbol(id="PTOYBTC")
    ZEC_USD = Symbol(id="ZECUSD")
    XEM_USD = Symbol(id="XEMUSD")
    BCN_USD = Symbol(id="BCNUSD")
    XDN_USD = Symbol(id="XDNUSD")
    MAID_USD = Symbol(id="MAIDUSD")
    ETC_BTC = Symbol(id="ETCBTC")
    ETC_USD = Symbol(id="ETCUSD")
    PLBT_BTC = Symbol(id="PLBTBTC")
    BNT_BTC = Symbol(id="BNTBTC")
    SNT_ETH = Symbol(id="SNTETH")
    CVC_USD = Symbol(id="CVCUSD")
    PAY_ETH = Symbol(id="PAYETH")
    OAX_ETH = Symbol(id="OAXETH")
    OMG_ETH = Symbol(id="OMGETH")
    BQX_ETH = Symbol(id="BQXETH")
    XTZ_BTC = Symbol(id="XTZBTC")
    DICE_BTC = Symbol(id="DICEBTC")
    PTOY_ETH = Symbol(id="PTOYETH")
    XAUR_ETH = Symbol(id="XAURETH")
    TIME_ETH = Symbol(id="TIMEETH")
    DICE_ETH = Symbol(id="DICEETH")
    SWT_ETH = Symbol(id="SWTETH")
    XMR_ETH = Symbol(id="XMRETH")
    ETC_ETH = Symbol(id="ETCETH")
    DASH_ETH = Symbol(id="DASHETH")
    ZEC_ETH = Symbol(id="ZECETH")
    PLU_ETH = Symbol(id="PLUETH")
    GNO_ETH = Symbol(id="GNOETH")
    XRP_BTC = Symbol(id="XRPBTC")
    STRAT_USD = Symbol(id="STRATUSD")
    STRAT_BTC = Symbol(id="STRATBTC")
    SNC_ETH = Symbol(id="SNCETH")
    ADX_ETH = Symbol(id="ADXETH")
    BET_ETH = Symbol(id="BETETH")
    EOS_ETH = Symbol(id="EOSETH")
    DENT_ETH = Symbol(id="DENTETH")
    SAN_ETH = Symbol(id="SANETH")
    EOS_BTC = Symbol(id="EOSBTC")
    EOS_USD = Symbol(id="EOSUSD")
    XTZ_ETH = Symbol(id="XTZETH")
    XTZ_USD = Symbol(id="XTZUSD")
    MYB_ETH = Symbol(id="MYBETH")
    SUR_ETH = Symbol(id="SURETH")
    IXT_ETH = Symbol(id="IXTETH")
    PLR_ETH = Symbol(id="PLRETH")
    TIX_ETH = Symbol(id="TIXETH")
    PRO_ETH = Symbol(id="PROETH")
    AVT_ETH = Symbol(id="AVTETH")
    EVX_USD = Symbol(id="EVXUSD")
    DLT_BTC = Symbol(id="DLTBTC")
    BNT_ETH = Symbol(id="BNTETH")
    BNT_USD = Symbol(id="BNTUSD")
    MANA_USD = Symbol(id="MANAUSD")
    DNT_BTC = Symbol(id="DNTBTC")
    FYP_BTC = Symbol(id="FYPBTC")
    OPT_BTC = Symbol(id="OPTBTC")
    TNT_ETH = Symbol(id="TNTETH")
    STX_BTC = Symbol(id="STXBTC")
    STX_ETH = Symbol(id="STXETH")
    STX_USD = Symbol(id="STXUSD")
    TNT_USD = Symbol(id="TNTUSD")
    TNT_BTC = Symbol(id="TNTBTC")
    CAT_BTC = Symbol(id="CATBTC")
    CAT_ETH = Symbol(id="CATETH")
    CAT_USD = Symbol(id="CATUSD")
    ENG_ETH = Symbol(id="ENGETH")
    XUC_USD = Symbol(id="XUCUSD")
    SNC_BTC = Symbol(id="SNCBTC")
    SNC_USD = Symbol(id="SNCUSD")
    OAX_USD = Symbol(id="OAXUSD")
    OAX_BTC = Symbol(id="OAXBTC")
    ZRX_BTC = Symbol(id="ZRXBTC")
    ZRX_ETH = Symbol(id="ZRXETH")
    ZRX_USD = Symbol(id="ZRXUSD")
    RVT_BTC = Symbol(id="RVTBTC")
    PPC_BTC = Symbol(id="PPCBTC")
    PPC_USD = Symbol(id="PPCUSD")
    QTUM_ETH = Symbol(id="QTUMETH")
    IGNIS_ETH = Symbol(id="IGNISETH")
    BMC_BTC = Symbol(id="BMCBTC")
    BMC_ETH = Symbol(id="BMCETH")
    BMC_USD = Symbol(id="BMCUSD")
    CND_BTC = Symbol(id="CNDBTC")
    CND_ETH = Symbol(id="CNDETH")
    CND_USD = Symbol(id="CNDUSD")
    CDT_ETH = Symbol(id="CDTETH")
    CDT_USD = Symbol(id="CDTUSD")
    FUN_BTC = Symbol(id="FUNBTC")
    FUN_ETH = Symbol(id="FUNETH")
    FUN_USD = Symbol(id="FUNUSD")
    HVN_BTC = Symbol(id="HVNBTC")
    HVN_ETH = Symbol(id="HVNETH")
    POE_BTC = Symbol(id="POEBTC")
    POE_ETH = Symbol(id="POEETH")
    AMB_USD = Symbol(id="AMBUSD")
    AMB_ETH = Symbol(id="AMBETH")
    AMB_BTC = Symbol(id="AMBBTC")
    HPC_BTC = Symbol(id="HPCBTC")
    PPT_ETH = Symbol(id="PPTETH")
    MTH_BTC = Symbol(id="MTHBTC")
    MTH_ETH = Symbol(id="MTHETH")
    LRC_BTC = Symbol(id="LRCBTC")
    LRC_ETH = Symbol(id="LRCETH")
    ICX_BTC = Symbol(id="ICXBTC")
    ICX_ETH = Symbol(id="ICXETH")
    NEO_BTC = Symbol(id="NEOBTC")
    NEO_ETH = Symbol(id="NEOETH")
    NEO_USD = Symbol(id="NEOUSD")
    CSNO_BTC = Symbol(id="CSNOBTC")
    ICX_USD = Symbol(id="ICXUSD")
    PIX_BTC = Symbol(id="PIXBTC")
    PIX_ETH = Symbol(id="PIXETH")
    IND_ETH = Symbol(id="INDETH")
    KICK_BTC = Symbol(id="KICKBTC")
    YOYOW_BTC = Symbol(id="YOYOWBTC")
    CDT_BTC = Symbol(id="CDTBTC")
    XVG_BTC = Symbol(id="XVGBTC")
    XVG_ETH = Symbol(id="XVGETH")
    XVG_USD = Symbol(id="XVGUSD")
    DGB_BTC = Symbol(id="DGBBTC")
    DGB_ETH = Symbol(id="DGBETH")
    DGB_USD = Symbol(id="DGBUSD")
    DCN_BTC = Symbol(id="DCNBTC")
    DCN_ETH = Symbol(id="DCNETH")
    DCN_USD = Symbol(id="DCNUSD")
    VIBE_BTC = Symbol(id="VIBEBTC")
    ENJ_BTC = Symbol(id="ENJBTC")
    ENJ_ETH = Symbol(id="ENJETH")
    ENJ_USD = Symbol(id="ENJUSD")
    ZSC_BTC = Symbol(id="ZSCBTC")
    ZSC_ETH = Symbol(id="ZSCETH")
    ZSC_USD = Symbol(id="ZSCUSD")
    TRX_BTC = Symbol(id="TRXBTC")
    TRX_ETH = Symbol(id="TRXETH")
    TRX_USD = Symbol(id="TRXUSD")
    ART_BTC = Symbol(id="ARTBTC")
    EVX_BTC = Symbol(id="EVXBTC")
    EVX_ETH = Symbol(id="EVXETH")
    SUB_BTC = Symbol(id="SUBBTC")
    SUB_ETH = Symbol(id="SUBETH")
    SUB_USD = Symbol(id="SUBUSD")
    WTC_BTC = Symbol(id="WTCBTC")
    BTM_BTC = Symbol(id="BTMBTC")
    BTM_ETH = Symbol(id="BTMETH")
    BTM_USD = Symbol(id="BTMUSD")
    LIFE_BTC = Symbol(id="LIFEBTC")
    VIB_BTC = Symbol(id="VIBBTC")
    VIB_ETH = Symbol(id="VIBETH")
    VIB_USD = Symbol(id="VIBUSD")
    DRT_ETH = Symbol(id="DRTETH")
    STU_USD = Symbol(id="STUUSD")
    OMG_BTC = Symbol(id="OMGBTC")
    PAY_BTC = Symbol(id="PAYBTC")
    PPT_BTC = Symbol(id="PPTBTC")
    SNT_BTC = Symbol(id="SNTBTC")
    BTG_BTC = Symbol(id="BTGBTC")
    BTG_ETH = Symbol(id="BTGETH")
    BTG_USD = Symbol(id="BTGUSD")
    SMART_BTC = Symbol(id="SMARTBTC")
    SMART_ETH = Symbol(id="SMARTETH")
    SMART_USD = Symbol(id="SMARTUSD")
    XUC_ETH = Symbol(id="XUCETH")
    XUC_BTC = Symbol(id="XUCBTC")
    LA_ETH = Symbol(id="LAETH")
    EDO_BTC = Symbol(id="EDOBTC")
    EDO_ETH = Symbol(id="EDOETH")
    EDO_USD = Symbol(id="EDOUSD")
    HGT_ETH = Symbol(id="HGTETH")
    IXT_BTC = Symbol(id="IXTBTC")
    SCL_BTC = Symbol(id="SCLBTC")
    ETP_BTC = Symbol(id="ETPBTC")
    ETP_ETH = Symbol(id="ETPETH")
    ETP_USD = Symbol(id="ETPUSD")
    DRPU_BTC = Symbol(id="DRPUBTC")
    NEBL_BTC = Symbol(id="NEBLBTC")
    NEBL_ETH = Symbol(id="NEBLETH")
    ARN_BTC = Symbol(id="ARNBTC")
    ARN_ETH = Symbol(id="ARNETH")
    STU_BTC = Symbol(id="STUBTC")
    STU_ETH = Symbol(id="STUETH")
    GVT_ETH = Symbol(id="GVTETH")
    BTX_BTC = Symbol(id="BTXBTC")
    LTC_ETH = Symbol(id="LTCETH")
    BCN_ETH = Symbol(id="BCNETH")
    MAID_ETH = Symbol(id="MAIDETH")
    NXT_ETH = Symbol(id="NXTETH")
    STRAT_ETH = Symbol(id="STRATETH")
    XDN_ETH = Symbol(id="XDNETH")
    XEM_ETH = Symbol(id="XEMETH")
    PLR_BTC = Symbol(id="PLRBTC")
    SUR_BTC = Symbol(id="SURBTC")
    BQX_BTC = Symbol(id="BQXBTC")
    DOGE_ETH = Symbol(id="DOGEETH")
    AMM_BTC = Symbol(id="AMMBTC")
    AMM_ETH = Symbol(id="AMMETH")
    AMM_USD = Symbol(id="AMMUSD")
    DBIX_BTC = Symbol(id="DBIXBTC")
    PRE_BTC = Symbol(id="PREBTC")
    ZAP_BTC = Symbol(id="ZAPBTC")
    DOV_BTC = Symbol(id="DOVBTC")
    DOV_ETH = Symbol(id="DOVETH")
    DRPU_ETH = Symbol(id="DRPUETH")
    XRP_ETH = Symbol(id="XRPETH")
    XRP_USD = Symbol(id="XRPUSDT")
    HSR_BTC = Symbol(id="HSRBTC")
    LEND_BTC = Symbol(id="LENDBTC")
    LEND_ETH = Symbol(id="LENDETH")
    SPF_ETH = Symbol(id="SPFETH")
    SBTC_BTC = Symbol(id="SBTCBTC")
    SBTC_ETH = Symbol(id="SBTCETH")
    LOC_BTC = Symbol(id="LOCBTC")
    LOC_ETH = Symbol(id="LOCETH")
    LOC_USD = Symbol(id="LOCUSD")
    SWFTC_BTC = Symbol(id="SWFTCBTC")
    SWFTC_ETH = Symbol(id="SWFTCETH")
    SWFTC_USD = Symbol(id="SWFTCUSD")
    STAR_ETH = Symbol(id="STARETH")
    SBTC_USD = Symbol(id="SBTCUSDT")
    STORM_BTC = Symbol(id="STORMBTC")
    DIM_ETH = Symbol(id="DIMETH")
    DIM_USD = Symbol(id="DIMUSD")
    DIM_BTC = Symbol(id="DIMBTC")
    NGC_BTC = Symbol(id="NGCBTC")
    NGC_ETH = Symbol(id="NGCETH")
    NGC_USD = Symbol(id="NGCUSD")
    EMC_ETH = Symbol(id="EMCETH")
    EMC_USD = Symbol(id="EMCUSDT")
    MCO_BTC = Symbol(id="MCOBTC")
    MCO_ETH = Symbol(id="MCOETH")
    MCO_USD = Symbol(id="MCOUSD")
    MANA_ETH = Symbol(id="MANAETH")
    MANA_BTC = Symbol(id="MANABTC")
    CPAY_ETH = Symbol(id="CPAYETH")
    DATA_BTC = Symbol(id="DATABTC")
    DATA_ETH = Symbol(id="DATAETH")
    DATA_USD = Symbol(id="DATAUSD")
    UTT_BTC = Symbol(id="UTTBTC")
    UTT_ETH = Symbol(id="UTTETH")
    UTT_USD = Symbol(id="UTTUSD")
    KMD_BTC = Symbol(id="KMDBTC")
    KMD_ETH = Symbol(id="KMDETH")
    KMD_USD = Symbol(id="KMDUSD")
    QTUM_USD = Symbol(id="QTUMUSD")
    QTUM_BTC = Symbol(id="QTUMBTC")
    SNT_USD = Symbol(id="SNTUSD")
    OMG_USD = Symbol(id="OMGUSD")
    EKO_BTC = Symbol(id="EKOBTC")
    EKO_ETH = Symbol(id="EKOETH")
    ADX_BTC = Symbol(id="ADXBTC")
    ADX_USD = Symbol(id="ADXUSD")
    LSK_ETH = Symbol(id="LSKETH")
    LSK_USD = Symbol(id="LSKUSD")
    PLR_USD = Symbol(id="PLRUSD")
    SUR_USD = Symbol(id="SURUSD")
    BQX_USD = Symbol(id="BQXUSD")
    DRT_USD = Symbol(id="DRTUSDT")
    REP_ETH = Symbol(id="REPETH")
    REP_USD = Symbol(id="REPUSDT")
    WAX_BTC = Symbol(id="WAXBTC")
    WAX_ETH = Symbol(id="WAXETH")
    WAX_USD = Symbol(id="WAXUSD")
    C20_BTC = Symbol(id="C20BTC")
    C20_ETH = Symbol(id="C20ETH")
    IDH_BTC = Symbol(id="IDHBTC")
    IDH_ETH = Symbol(id="IDHETH")
    IPL_BTC = Symbol(id="IPLBTC")
    COV_BTC = Symbol(id="COVBTC")
    COV_ETH = Symbol(id="COVETH")
    SENT_BTC = Symbol(id="SENTBTC")
    SENT_ETH = Symbol(id="SENTETH")
    SENT_USD = Symbol(id="SENTUSD")
    SMT_BTC = Symbol(id="SMTBTC")
    SMT_ETH = Symbol(id="SMTETH")
    SMT_USD = Symbol(id="SMTUSD")
    CVH_ETH = Symbol(id="CVHETH")
    CVH_USD = Symbol(id="CVHUSD")
    CHAT_BTC = Symbol(id="CHATBTC")
    CHAT_ETH = Symbol(id="CHATETH")
    CHAT_USD = Symbol(id="CHATUSD")
    TRAC_ETH = Symbol(id="TRACETH")
    JNT_ETH = Symbol(id="JNTETH")
    UTK_BTC = Symbol(id="UTKBTC")
    UTK_ETH = Symbol(id="UTKETH")
    UTK_USD = Symbol(id="UTKUSD")
    GNX_ETH = Symbol(id="GNXETH")
    CHSB_BTC = Symbol(id="CHSBBTC")
    CHSB_ETH = Symbol(id="CHSBETH")
    DAY_BTC = Symbol(id="DAYBTC")
    DAY_ETH = Symbol(id="DAYETH")
    DAY_USD = Symbol(id="DAYUSD")
    NEU_BTC = Symbol(id="NEUBTC")
    NEU_ETH = Symbol(id="NEUETH")
    NEU_USD = Symbol(id="NEUUSD")
    TAU_BTC = Symbol(id="TAUBTC")
    FLP_BTC = Symbol(id="FLPBTC")
    FLP_ETH = Symbol(id="FLPETH")
    FLP_USD = Symbol(id="FLPUSD")
    R_BTC = Symbol(id="RBTC")
    R_ETH = Symbol(id="RETH")
    EKO_USD = Symbol(id="EKOUSDT")
    BCPT_ETH = Symbol(id="BCPTETH")
    BCPT_USD = Symbol(id="BCPTUSDT")
    PKT_BTC = Symbol(id="PKTBTC")
    PKT_ETH = Symbol(id="PKTETH")
    BETR_BTC = Symbol(id="BETRBTC")
    BETR_ETH = Symbol(id="BETRETH")
    RNTB_ETH = Symbol(id="RNTBETH")
    HAND_ETH = Symbol(id="HANDETH")
    HAND_USD = Symbol(id="HANDUSD")
    ACO_ETH = Symbol(id="ACOETH")
    CPY_BTC = Symbol(id="CPYBTC")
    CPY_ETH = Symbol(id="CPYETH")
    CHP_ETH = Symbol(id="CHPETH")
    BCPT_BTC = Symbol(id="BCPTBTC")
    ACT_BTC = Symbol(id="ACTBTC")
    ACT_ETH = Symbol(id="ACTETH")
    ACT_USD = Symbol(id="ACTUSD")
    ADA_BTC = Symbol(id="ADABTC")
    ADA_ETH = Symbol(id="ADAETH")
    ADA_USD = Symbol(id="ADAUSD")
    MTX_BTC = Symbol(id="MTXBTC")
    MTX_ETH = Symbol(id="MTXETH")
    MTX_USD = Symbol(id="MTXUSD")
    WIZ_BTC = Symbol(id="WIZBTC")
    WIZ_ETH = Symbol(id="WIZETH")
    WIZ_USD = Symbol(id="WIZUSD")
    DADI_BTC = Symbol(id="DADIBTC")
    DADI_ETH = Symbol(id="DADIETH")
    BDG_ETH = Symbol(id="BDGETH")
    DATX_BTC = Symbol(id="DATXBTC")
    DATX_ETH = Symbol(id="DATXETH")
    TRUE_BTC = Symbol(id="TRUEBTC")
    DRG_BTC = Symbol(id="DRGBTC")
    DRG_ETH = Symbol(id="DRGETH")
    BANCA_BTC = Symbol(id="BANCABTC")
    BANCA_ETH = Symbol(id="BANCAETH")
    ZAP_ETH = Symbol(id="ZAPETH")
    ZAP_USD = Symbol(id="ZAPUSD")
    AUTO_BTC = Symbol(id="AUTOBTC")
    NOAH_BTC = Symbol(id="NOAHBTC")
    SOC_BTC = Symbol(id="SOCBTC")
    OCN_BTC = Symbol(id="OCNBTC")
    OCN_ETH = Symbol(id="OCNETH")
    STQ_BTC = Symbol(id="STQBTC")
    STQ_ETH = Symbol(id="STQETH")
    XLM_BTC = Symbol(id="XLMBTC")
    XLM_ETH = Symbol(id="XLMETH")
    XLM_USD = Symbol(id="XLMUSD")
    IOTA_BTC = Symbol(id="IOTABTC")
    IOTA_ETH = Symbol(id="IOTAETH")
    IOTA_USD = Symbol(id="IOTAUSD")
    DRT_BTC = Symbol(id="DRTBTC")
    BETR_USD = Symbol(id="BETRUSD")
    ERT_BTC = Symbol(id="ERTBTC")
    CRPT_BTC = Symbol(id="CRPTBTC")
    CRPT_USD = Symbol(id="CRPTUSD")
    MESH_BTC = Symbol(id="MESHBTC")
    MESH_ETH = Symbol(id="MESHETH")
    MESH_USD = Symbol(id="MESHUSD")
    IHT_BTC = Symbol(id="IHTBTC")
    IHT_ETH = Symbol(id="IHTETH")
    IHT_USD = Symbol(id="IHTUSD")
    SCC_BTC = Symbol(id="SCCBTC")
    YCC_BTC = Symbol(id="YCCBTC")
    DAN_BTC = Symbol(id="DANBTC")
    TEL_BTC = Symbol(id="TELBTC")
    TEL_ETH = Symbol(id="TELETH")
    NCT_BTC = Symbol(id="NCTBTC")
    NCT_ETH = Symbol(id="NCTETH")
    NCT_USD = Symbol(id="NCTUSD")
    BMH_BTC = Symbol(id="BMHBTC")
    BANCA_USD = Symbol(id="BANCAUSD")
    NOAH_ETH = Symbol(id="NOAHETH")
    NOAH_USD = Symbol(id="NOAHUSD")
    BERRY_BTC = Symbol(id="BERRYBTC")
    BERRY_ETH = Symbol(id="BERRYETH")
    BERRY_USD = Symbol(id="BERRYUSD")
    GBX_BTC = Symbol(id="GBXBTC")
    GBX_ETH = Symbol(id="GBXETH")
    GBX_USD = Symbol(id="GBXUSD")
    SHIP_BTC = Symbol(id="SHIPBTC")
    SHIP_ETH = Symbol(id="SHIPETH")
    NANO_BTC = Symbol(id="NANOBTC")
    NANO_ETH = Symbol(id="NANOETH")
    NANO_USD = Symbol(id="NANOUSD")
    LNC_BTC = Symbol(id="LNCBTC")
    KIN_ETH = Symbol(id="KINETH")
    ARDR_USD = Symbol(id="ARDRUSD")
    FOTA_ETH = Symbol(id="FOTAETH")
    FOTA_BTC = Symbol(id="FOTABTC")
    CVT_BTC = Symbol(id="CVTBTC")
    CVT_ETH = Symbol(id="CVTETH")
    CVT_USD = Symbol(id="CVTUSD")
    STQ_USD = Symbol(id="STQUSD")
    GNT_BTC = Symbol(id="GNTBTC")
    GNT_ETH = Symbol(id="GNTETH")
    GNT_USD = Symbol(id="GNTUSD")
    ADH_BTC = Symbol(id="ADHBTC")
    ADH_ETH = Symbol(id="ADHETH")
    GET_BTC = Symbol(id="GETBTC")
    MITH_BTC = Symbol(id="MITHBTC")
    MITH_ETH = Symbol(id="MITHETH")
    MITH_USD = Symbol(id="MITHUSD")
    SUNC_ETH = Symbol(id="SUNCETH")
    DADI_USD = Symbol(id="DADIUSD")
    TKY_BTC = Symbol(id="TKYBTC")
    ACAT_BTC = Symbol(id="ACATBTC")
    ACAT_ETH = Symbol(id="ACATETH")
    ACAT_USD = Symbol(id="ACATUSD")
    BTX_USD = Symbol(id="BTXUSD")
    WIKI_BTC = Symbol(id="WIKIBTC")
    WIKI_ETH = Symbol(id="WIKIETH")
    WIKI_USD = Symbol(id="WIKIUSD")
    ONT_BTC = Symbol(id="ONTBTC")
    ONT_ETH = Symbol(id="ONTETH")
    ONT_USD = Symbol(id="ONTUSD")
    FTX_BTC = Symbol(id="FTXBTC")
    FTX_ETH = Symbol(id="FTXETH")
    FREC_BTC = Symbol(id="FRECBTC")
    NAVI_BTC = Symbol(id="NAVIBTC")
    FREC_ETH = Symbol(id="FRECETH")
    FREC_USD = Symbol(id="FRECUSDT")
    VME_ETH = Symbol(id="VMEETH")
    NAVI_ETH = Symbol(id="NAVIETH")
    LND_ETH = Symbol(id="LNDETH")
    CSM_BTC = Symbol(id="CSMBTC")
    NANJ_BTC = Symbol(id="NANJBTC")
    NTK_BTC = Symbol(id="NTKBTC")
    NTK_ETH = Symbol(id="NTKETH")
    NTK_USD = Symbol(id="NTKUSD")
    AUC_BTC = Symbol(id="AUCBTC")
    AUC_ETH = Symbol(id="AUCETH")
    CMCT_BTC = Symbol(id="CMCTBTC")
    CMCT_ETH = Symbol(id="CMCTETH")
    CMCT_USD = Symbol(id="CMCTUSD")
    MAN_BTC = Symbol(id="MANBTC")
    MAN_ETH = Symbol(id="MANETH")
    MAN_USD = Symbol(id="MANUSD")
    PNT_BTC = Symbol(id="PNTBTC")
    PNT_ETH = Symbol(id="PNTETH")
    FXT_BTC = Symbol(id="FXTBTC")
    NEXO_BTC = Symbol(id="NEXOBTC")
    PAT_BTC = Symbol(id="PATBTC")
    PAT_ETH = Symbol(id="PATETH")
    XMC_BTC = Symbol(id="XMCBTC")
    FXT_ETH = Symbol(id="FXTETH")
    HERO_BTC = Symbol(id="HEROBTC")
    HERO_ETH = Symbol(id="HEROETH")
    XMC_ETH = Symbol(id="XMCETH")
    XMC_USD = Symbol(id="XMCUSDT")
    FDZ_BTC = Symbol(id="FDZBTC")
    FDZ_ETH = Symbol(id="FDZETH")
    FDZ_USD = Symbol(id="FDZUSD")
    SPD_BTC = Symbol(id="SPDBTC")
    SPD_ETH = Symbol(id="SPDETH")
    MITX_BTC = Symbol(id="MITXBTC")
    TIV_BTC = Symbol(id="TIVBTC")
    B2G_BTC = Symbol(id="B2GBTC")
    B2G_USD = Symbol(id="B2GUSD")
    ZPT_BTC = Symbol(id="ZPTBTC")
    ZPT_ETH = Symbol(id="ZPTETH")
    HBZ_BTC = Symbol(id="HBZBTC")
    FACE_BTC = Symbol(id="FACEBTC")
    FACE_ETH = Symbol(id="FACEETH")
    HBZ_ETH = Symbol(id="HBZETH")
    HBZ_USD = Symbol(id="HBZUSD")
    ZPT_USD = Symbol(id="ZPTUSD")
    CPT_BTC = Symbol(id="CPTBTC")
    PAT_USD = Symbol(id="PATUSD")
    HTML_BTC = Symbol(id="HTMLBTC")
    HTML_ETH = Symbol(id="HTMLETH")
    MITX_ETH = Symbol(id="MITXETH")
    JOT_BTC = Symbol(id="JOTBTC")
    JBC_BTC = Symbol(id="JBCBTC")
    JBC_ETH = Symbol(id="JBCETH")
    BTS_BTC = Symbol(id="BTSBTC")
    BNK_BTC = Symbol(id="BNKBTC")
    KBC_BTC = Symbol(id="KBCBTC")
    KBC_ETH = Symbol(id="KBCETH")
    BNK_ETH = Symbol(id="BNKETH")
    BNK_USD = Symbol(id="BNKUSD")
    TIV_ETH = Symbol(id="TIVETH")
    TIV_USD = Symbol(id="TIVUSD")
    CSM_ETH = Symbol(id="CSMETH")
    CSM_USD = Symbol(id="CSMUSD")
    INK_BTC = Symbol(id="INKBTC")
    IOST_BTC = Symbol(id="IOSTBTC")
    INK_ETH = Symbol(id="INKETH")
    INK_USD = Symbol(id="INKUSD")
    CBC_BTC = Symbol(id="CBCBTC")
    IOST_USD = Symbol(id="IOSTUSD")
    ZIL_BTC = Symbol(id="ZILBTC")
    PMNT_BTC = Symbol(id="PMNTBTC")
    ABYSS_BTC = Symbol(id="ABYSSBTC")
    ABYSS_ETH = Symbol(id="ABYSSETH")
    ZIL_USD = Symbol(id="ZILUSD")
    BCI_BTC = Symbol(id="BCIBTC")
    CBC_ETH = Symbol(id="CBCETH")
    CBC_USD = Symbol(id="CBCUSD")
    PITCH_BTC = Symbol(id="PITCHBTC")
    PITCH_ETH = Symbol(id="PITCHETH")
    HTML_USD = Symbol(id="HTMLUSD")
    TDS_BTC = Symbol(id="TDSBTC")
    TDS_ETH = Symbol(id="TDSETH")
    TDS_USD = Symbol(id="TDSUSD")
    SBD_ETH = Symbol(id="SBDETH")
    SBD_USD = Symbol(id="SBDUSD")
    DPN_BTC = Symbol(id="DPNBTC")
    UUU_BTC = Symbol(id="UUUBTC")
    UUU_ETH = Symbol(id="UUUETH")
    XBP_BTC = Symbol(id="XBPBTC")
    CLN_BTC = Symbol(id="CLNBTC")
    CLN_ETH = Symbol(id="CLNETH")
    ELEC_BTC = Symbol(id="ELECBTC")
    ELEC_ETH = Symbol(id="ELECETH")
    ELEC_USD = Symbol(id="ELECUSD")
    QNTU_BTC = Symbol(id="QNTUBTC")
    QNTU_ETH = Symbol(id="QNTUETH")
    QNTU_USD = Symbol(id="QNTUUSD")
    IPL_ETH = Symbol(id="IPLETH")
    IPL_USD = Symbol(id="IPLUSD")
    CENNZ_BTC = Symbol(id="CENNZBTC")
    CENNZ_ETH = Symbol(id="CENNZETH")
    SWM_BTC = Symbol(id="SWMBTC")
    SPF_USD = Symbol(id="SPFUSD")
    SPF_BTC = Symbol(id="SPFBTC")
    KRM_USD = Symbol(id="KRMUSD")
    LCC_BTC = Symbol(id="LCCBTC")
    HGT_BTC = Symbol(id="HGTBTC")
    ETH_TUSD = Symbol(id="ETHTUSD")
    BTC_TUSD = Symbol(id="BTCTUSD")
    LTC_TUSD = Symbol(id="LTCTUSD")
    XMR_TUSD = Symbol(id="XMRTUSD")
    ZRX_TUSD = Symbol(id="ZRXTUSD")
    NEO_TUSD = Symbol(id="NEOTUSD")
    USD_TUSD = Symbol(id="USDTUSD")
    BTC_DAI = Symbol(id="BTCDAI")
    ETH_DAI = Symbol(id="ETHDAI")
    MKR_DAI = Symbol(id="MKRDAI")
    EOS_DAI = Symbol(id="EOSDAI")
    USD_DAI = Symbol(id="USDDAI")
    MKR_BTC = Symbol(id="MKRBTC")
    MKR_ETH = Symbol(id="MKRETH")
    MKR_USD = Symbol(id="MKRUSD")
    TUSD_DAI = Symbol(id="TUSDDAI")
    NEO_DAI = Symbol(id="NEODAI")
    LTC_DAI = Symbol(id="LTCDAI")
    XMR_DAI = Symbol(id="XMRDAI")
    XRP_DAI = Symbol(id="XRPDAI")
    NEXO_ETH = Symbol(id="NEXOETH")
    NEXO_USD = Symbol(id="NEXOUSD")
    DWS_BTC = Symbol(id="DWSBTC")
    DWS_ETH = Symbol(id="DWSETH")
    DWS_USD = Symbol(id="DWSUSD")
    APPC_BTC = Symbol(id="APPCBTC")
    APPC_ETH = Symbol(id="APPCETH")
    APPC_USD = Symbol(id="APPCUSD")
    BIT_ETH = Symbol(id="BITETH")
    SPC_BTC = Symbol(id="SPCBTC")
    SPC_ETH = Symbol(id="SPCETH")
    SPC_USD = Symbol(id="SPCUSD")
    REX_BTC = Symbol(id="REXBTC")
    REX_ETH = Symbol(id="REXETH")
    REX_USD = Symbol(id="REXUSD")
    ELF_BTC = Symbol(id="ELFBTC")
    ELF_USD = Symbol(id="ELFUSD")
    BCD_BTC = Symbol(id="BCDBTC")
    BCD_USD = Symbol(id="BCDUSD")
    CVCOIN_BTC = Symbol(id="CVCOINBTC")
    CVCOIN_ETH = Symbol(id="CVCOINETH")
    CVCOIN_USD = Symbol(id="CVCOINUSD")
    EDG_ETH = Symbol(id="EDGETH")
    EDG_USD = Symbol(id="EDGUSD")
    NLC2_BTC = Symbol(id="NLC2BTC")
    COSM_BTC = Symbol(id="COSMBTC")
    COSM_ETH = Symbol(id="COSMETH")
    DASH_EURS = Symbol(id="DASHEURS")
    ZEC_EURS = Symbol(id="ZECEURS")
    BTC_EURS = Symbol(id="BTCEURS")
    EOS_EURS = Symbol(id="EOSEURS")
    ETH_EURS = Symbol(id="ETHEURS")
    LTC_EURS = Symbol(id="LTCEURS")
    NEO_EURS = Symbol(id="NEOEURS")
    XMR_EURS = Symbol(id="XMREURS")
    XRP_EURS = Symbol(id="XRPEURS")
    EURS_USD = Symbol(id="EURSUSD")
    EURS_TUSD = Symbol(id="EURSTUSD")
    EURS_DAI = Symbol(id="EURSDAI")
    MNX_USD = Symbol(id="MNXUSD")
    ROX_ETH = Symbol(id="ROXETH")
    ZPR_ETH = Symbol(id="ZPRETH")
    MNX_BTC = Symbol(id="MNXBTC")
    MNX_ETH = Symbol(id="MNXETH")
    KIND_BTC = Symbol(id="KINDBTC")
    KIND_ETH = Symbol(id="KINDETH")
    ENGT_BTC = Symbol(id="ENGTBTC")
    ENGT_ETH = Symbol(id="ENGTETH")
    PMA_BTC = Symbol(id="PMABTC")
    PMA_ETH = Symbol(id="PMAETH")
    TV_BTC = Symbol(id="TVBTC")
    TV_ETH = Symbol(id="TVETH")
    TV_USD = Symbol(id="TVUSD")
    XCLR_BTC = Symbol(id="XCLRBTC")
    BAT_BTC = Symbol(id="BATBTC")
    BAT_ETH = Symbol(id="BATETH")
    BAT_USD = Symbol(id="BATUSD")
    SRN_BTC = Symbol(id="SRNBTC")
    SRN_ETH = Symbol(id="SRNETH")
    SRN_USD = Symbol(id="SRNUSD")
    SVD_BTC = Symbol(id="SVDBTC")
    SVD_ETH = Symbol(id="SVDETH")
    SVD_USD = Symbol(id="SVDUSD")
    GST_BTC = Symbol(id="GSTBTC")
    GST_ETH = Symbol(id="GSTETH")
    GST_USD = Symbol(id="GSTUSD")
    BNB_BTC = Symbol(id="BNBBTC")
    BNB_ETH = Symbol(id="BNBETH")
    BNB_USD = Symbol(id="BNBUSD")
    DIT_BTC = Symbol(id="DITBTC")
    DIT_ETH = Symbol(id="DITETH")
    POA20_BTC = Symbol(id="POA20BTC")
    CCL_USD = Symbol(id="CCLUSD")
    PROC_BTC = Symbol(id="PROCBTC")
    POA20_ETH = Symbol(id="POA20ETH")
    POA20_USD = Symbol(id="POA20USD")
    POA20_DAI = Symbol(id="POA20DAI")
    NIM_BTC = Symbol(id="NIMBTC")
    USE_BTC = Symbol(id="USEBTC")
    USE_ETH = Symbol(id="USEETH")
    DAV_BTC = Symbol(id="DAVBTC")
    DAV_ETH = Symbol(id="DAVETH")
    ABTC_BTC = Symbol(id="ABTCBTC")
    NIM_ETH = Symbol(id="NIMETH")
    ABA_BTC = Symbol(id="ABABTC")
    ABA_ETH = Symbol(id="ABAETH")
    ABA_USD = Symbol(id="ABAUSD")
    BCN_EOS = Symbol(id="BCNEOS")
    LTC_EOS = Symbol(id="LTCEOS")
    XMR_EOS = Symbol(id="XMREOS")
    DASH_EOS = Symbol(id="DASHEOS")
    TRX_EOS = Symbol(id="TRXEOS")
    NEO_EOS = Symbol(id="NEOEOS")
    ZEC_EOS = Symbol(id="ZECEOS")
    LSK_EOS = Symbol(id="LSKEOS")
    XEM_EOS = Symbol(id="XEMEOS")
    XRP_EOS = Symbol(id="XRPEOS")
    MESSE_BTC = Symbol(id="MESSEBTC")
    MESSE_ETH = Symbol(id="MESSEETH")
    MESSE_USD = Symbol(id="MESSEUSD")
    CCL_ETH = Symbol(id="CCLETH")
    RCN_BTC = Symbol(id="RCNBTC")
    RCN_ETH = Symbol(id="RCNETH")
    RCN_USD = Symbol(id="RCNUSD")
    HMQ_BTC = Symbol(id="HMQBTC")
    HMQ_ETH = Symbol(id="HMQETH")
    MYST_BTC = Symbol(id="MYSTBTC")
    MYST_ETH = Symbol(id="MYSTETH")
    USD_GUSD = Symbol(id="USDTGUSD")
    BTC_GUSD = Symbol(id="BTCGUSD")
    ETH_GUSD = Symbol(id="ETHGUSD")
    EOS_GUSD = Symbol(id="EOSGUSD")
    AXPR_BTC = Symbol(id="AXPRBTC")
    AXPR_ETH = Symbol(id="AXPRETH")
    DAG_BTC = Symbol(id="DAGBTC")
    DAG_ETH = Symbol(id="DAGETH")
    BITS_BTC = Symbol(id="BITSBTC")
    BITS_ETH = Symbol(id="BITSETH")
    BITS_USD = Symbol(id="BITSUSD")
    CDCC_BTC = Symbol(id="CDCCBTC")
    CDCC_ETH = Symbol(id="CDCCETH")
    CDCC_USD = Symbol(id="CDCCUSD")
    VET_BTC = Symbol(id="VETBTC")
    VET_ETH = Symbol(id="VETETH")
    VET_USD = Symbol(id="VETUSDT")
    SILK_ETH = Symbol(id="SILKETH")
    BOX_BTC = Symbol(id="BOXBTC")
    BOX_ETH = Symbol(id="BOXETH")
    BOX_EURS = Symbol(id="BOXEURS")
    BOX_EOS = Symbol(id="BOXEOS")
    VOCO_BTC = Symbol(id="VOCOBTC")
    VOCO_ETH = Symbol(id="VOCOETH")
    VOCO_USD = Symbol(id="VOCOUSD")
    PASS_BTC = Symbol(id="PASSBTC")
    PASS_ETH = Symbol(id="PASSETH")
    SLX_BTC = Symbol(id="SLXBTC")
    SLX_USD = Symbol(id="SLXUSD")
    PBTT_BTC = Symbol(id="PBTTBTC")
    PMA_USD = Symbol(id="PMAUSD")
    TRAD_BTC = Symbol(id="TRADBTC")
    DGTX_BTC = Symbol(id="DGTXBTC")
    DGTX_ETH = Symbol(id="DGTXETH")
    DGTX_USD = Symbol(id="DGTXUSD")
    MRK_BTC = Symbol(id="MRKBTC")
    MRK_ETH = Symbol(id="MRKETH")
    DGB_TUSD = Symbol(id="DGBTUSD")
    MESSE_EOS = Symbol(id="MESSEEOS")
    MESSE_EURS = Symbol(id="MESSEEURS")
    SNBL_BTC = Symbol(id="SNBLBTC")
    BCH_BTC = Symbol(id="BCHBTC")
    BCH_USD = Symbol(id="BCHUSD")
    BSV_BTC = Symbol(id="BSVBTC")
    BSV_USD = Symbol(id="BSVUSD")
    BKX_BTC = Symbol(id="BKXBTC")
    NPLC_BTC = Symbol(id="NPLCBTC")
    NPLC_ETH = Symbol(id="NPLCETH")
    ETN_BTC = Symbol(id="ETNBTC")
    ETN_ETH = Symbol(id="ETNETH")
    ETN_USD = Symbol(id="ETNUSD")
    MRS_BTC = Symbol(id="MRSBTC")
    MRS_ETH = Symbol(id="MRSETH")
    MRS_USD = Symbol(id="MRSUSD")
    DTR_BTC = Symbol(id="DTRBTC")
    DTR_ETH = Symbol(id="DTRETH")
    TDP_BTC = Symbol(id="TDPBTC")
    HBT_ETH = Symbol(id="HBTETH")
    PXG_BTC = Symbol(id="PXGBTC")
    PXG_USD = Symbol(id="PXGUSD")
    BTC_PAX = Symbol(id="BTCPAX")
    ETH_PAX = Symbol(id="ETHPAX")
    USD_PAX = Symbol(id="USDPAX")
    BTC_USDC = Symbol(id="BTCUSDC")
    ETH_USDC = Symbol(id="ETHUSDC")
    USD_USDC = Symbol(id="USDUSDC")
    TUSD_USDC = Symbol(id="TUSDUSDC")
    DAI_USDC = Symbol(id="DAIUSDC")
    EOS_PAX = Symbol(id="EOSPAX")
    CLO_BTC = Symbol(id="CLOBTC")
    CLO_ETH = Symbol(id="CLOETH")
    CLO_USD = Symbol(id="CLOUSD")
    PETH_BTC = Symbol(id="PETHBTC")
    PETH_ETH = Symbol(id="PETHETH")
    PETH_USD = Symbol(id="PETHUSD")
    BRD_BTC = Symbol(id="BRDBTC")
    BRD_ETH = Symbol(id="BRDETH")
    NMR_BTC = Symbol(id="NMRBTC")
    SALT_BTC = Symbol(id="SALTBTC")
    SALT_ETH = Symbol(id="SALTETH")
    POLY_BTC = Symbol(id="POLYBTC")
    POLY_ETH = Symbol(id="POLYETH")
    POWR_BTC = Symbol(id="POWRBTC")
    POWR_ETH = Symbol(id="POWRETH")
    STORJ_BTC = Symbol(id="STORJBTC")
    STORJ_ETH = Symbol(id="STORJETH")
    STORJ_USD = Symbol(id="STORJUSD")
    MLN_BTC = Symbol(id="MLNBTC")
    MLN_ETH = Symbol(id="MLNETH")
    BDG_BTC = Symbol(id="BDGBTC")
    POA_ETH = Symbol(id="POAETH")
    POA_BTC = Symbol(id="POABTC")
    POA_USD = Symbol(id="POAUSD")
    POA_DAI = Symbol(id="POADAI")
    KIN_BTC = Symbol(id="KINBTC")
    VEO_BTC = Symbol(id="VEOBTC")
    PLA_BTC = Symbol(id="PLABTC")
    PLA_ETH = Symbol(id="PLAETH")
    PLA_USD = Symbol(id="PLAUSD")
    BTT_BTC = Symbol(id="BTTBTC")
    BTT_USD = Symbol(id="BTTUSD")
    BTT_ETH = Symbol(id="BTTETH")
    ZEN_BTC = Symbol(id="ZENBTC")
    ZEN_ETH = Symbol(id="ZENETH")
    ZEN_USD = Symbol(id="ZENUSD")
    GRIN_BTC = Symbol(id="GRINBTC")
    GRIN_ETH = Symbol(id="GRINETH")
    GRIN_USD = Symbol(id="GRINUSD")
    FET_BTC = Symbol(id="FETBTC")
    HT_BTC = Symbol(id="HTBTC")
    HT_USD = Symbol(id="HTUSD")
    XZC_BTC = Symbol(id="XZCBTC")
    XZC_ETH = Symbol(id="XZCETH")
    XZC_USD = Symbol(id="XZCUSD")
    VRA_BTC = Symbol(id="VRABTC")
    VRA_ETH = Symbol(id="VRAETH")
    BTC_KRWB = Symbol(id="BTCKRWB")
    USD_KRWB = Symbol(id="USDKRWB")
    WBTC_ETH = Symbol(id="WBTCETH")
    CRO_BTC = Symbol(id="CROBTC")
    CRO_ETH = Symbol(id="CROETH")
    CRO_USD = Symbol(id="CROUSD")
    GAS_BTC = Symbol(id="GASBTC")
    GAS_ETH = Symbol(id="GASETH")
    GAS_USD = Symbol(id="GASUSD")
    ORMEUS_BTC = Symbol(id="ORMEUSBTC")
    ORMEUS_ETH = Symbol(id="ORMEUSETH")
    SWM_ETH = Symbol(id="SWMETH")
    SWM_USD = Symbol(id="SWMUSD")
    PRE_ETH = Symbol(id="PREETH")
    PHX_BTC = Symbol(id="PHXBTC")
    PHX_ETH = Symbol(id="PHXETH")
    PHX_USD = Symbol(id="PHXUSD")
    BET_BTC = Symbol(id="BETBTC")
    USD_EOSDT = Symbol(id="USDEOSDT")
    BTC_EOSDT = Symbol(id="BTCEOSDT")
    ETH_EOSDT = Symbol(id="ETHEOSDT")
    EOS_EOSDT = Symbol(id="EOSEOSDT")
    DAI_EOSDT = Symbol(id="DAIEOSDT")
    NUT_BTC = Symbol(id="NUTBTC")
    NUT_EOS = Symbol(id="NUTEOS")
    NUT_USD = Symbol(id="NUTUSD")
    CUTE_BTC = Symbol(id="CUTEBTC")
    CUTE_ETH = Symbol(id="CUTEETH")
    CUTE_USD = Symbol(id="CUTEUSD")
    CUTE_EOS = Symbol(id="CUTEEOS")
    XCON_BTC = Symbol(id="XCONBTC")
    DCR_BTC = Symbol(id="DCRBTC")
    DCR_ETH = Symbol(id="DCRETH")
    DCR_USD = Symbol(id="DCRUSD")
    MG_BTC = Symbol(id="MGBTC")
    MG_ETH = Symbol(id="MGETH")
    MG_EOS = Symbol(id="MGEOS")
    MG_USD = Symbol(id="MGUSD")
    GNX_BTC = Symbol(id="GNXBTC")
    PRO_BTC = Symbol(id="PROBTC")
    EURS_EOSDT = Symbol(id="EURSEOSDT")
    TUSD_EOSDT = Symbol(id="TUSDEOSDT")
    ECOIN_BTC = Symbol(id="ECOINBTC")
    ECOIN_ETH = Symbol(id="ECOINETH")
    ECOIN_USD = Symbol(id="ECOINUSD")
    AGI_BTC = Symbol(id="AGIBTC")
    LOOM_BTC = Symbol(id="LOOMBTC")
    LOOM_ETH = Symbol(id="LOOMETH")
    BLZ_BTC = Symbol(id="BLZBTC")
    QKC_BTC = Symbol(id="QKCBTC")
    QKC_ETH = Symbol(id="QKCETH")
    KNC_BTC = Symbol(id="KNCBTC")
    KNC_ETH = Symbol(id="KNCETH")
    KNC_USD = Symbol(id="KNCUSD")
    KEY_BTC = Symbol(id="KEYBTC")
    KEY_ETH = Symbol(id="KEYETH")
    ATOM_BTC = Symbol(id="ATOMBTC")
    ATOM_USD = Symbol(id="ATOMUSD")
    ATOM_ETH = Symbol(id="ATOMETH")
    BRDG_BTC = Symbol(id="BRDGBTC")
    BRDG_ETH = Symbol(id="BRDGETH")
    BRDG_USD = Symbol(id="BRDGUSD")
    MTL_BTC = Symbol(id="MTLBTC")
    MTL_ETH = Symbol(id="MTLETH")
    EXP_BTC = Symbol(id="EXPBTC")
    BTCB_BTC = Symbol(id="BTCBBTC")
    PBT_BTC = Symbol(id="PBTBTC")
    PBT_ETH = Symbol(id="PBTETH")
    LINK_BTC = Symbol(id="LINKBTC")
    LINK_ETH = Symbol(id="LINKETH")
    LINK_USD = Symbol(id="LINKUSD")
    USD_USDT20 = Symbol(id="USDUSDT20")
    PHB_BTC = Symbol(id="PHBBTC")
    BCH_ETH = Symbol(id="BCHETH")
    BCH_DAI = Symbol(id="BCHDAI")
    BCH_TUSD = Symbol(id="BCHTUSD")
    BCH_EURS = Symbol(id="BCHEURS")