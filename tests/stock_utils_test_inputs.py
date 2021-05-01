"""
INPUTS and EXPECTED OUTPUTS FOR STOCK_UTILS_TEST.PY
"""

INPUT1 = [{
    'Mega': {
        'CSCO': {
            'Symbol':
            'CSCO',
            'Company':
            'Cisco Systems, Inc.',
            'High':
            53.59,
            'Low':
            51.54,
            'Price':
            51.76,
            'Category':
            'Mega',
            'Overview':
            'o oaobusmesauihypgi  iretg pfeoepr lilli irItregwetnafinnostnelureglrfonr wigewun c tuslrus a u  aoCnmt iodyws ahu nfi bri rntssdv y n itrner h  oawiyn ,olr c.ote gedasidosipctahcctenonntauopl  . ictC aaoseycr nnemuiierbrposaesiri eey ardt,dieigsrts,m'
        },
        'UNH': {
            'Symbol': 'UNH',
            'Company': 'Unitedhealth Group Inc',
            'High': 406.03,
            'Low': 400.07,
            'Price': 400.4,
            'Category': 'Mega',
            'Overview': '0'
        },
        'KO': {
            'Symbol':
            'KO',
            'Company':
            'Coca-Cola Co',
            'High':
            56.68,
            'Low':
            53.7,
            'Price':
            56.11,
            'Category':
            'Mega',
            'Overview':
            "eTlogtofrbsftwi,cre0pel.h,shwirpdpiyraocmasnc- iohbF rd-acagri to mt p diieub0ayanr Moieb  n ice  isdtb ah pSlTit,nontoe su.etp nC g,r  al   nHickseCocde  o hiinouatisrii iT yProsaeiieg ehpaeiys radpv  htof llddotfrynuedlotoneloofrmvnnpso, ir  aoboccaSdgueto aldedsattron la yl0 rsr ny eo cah  vsgcfill,kre mrpi odeaugmnsarneoao r cciefi i-eaduhtnol  Gm r.ig f iisooc gtneeonasr amelCo nittlegbeaa,.o r o,lkle T, weosi o mae,ti   atrcfe nashtrea rwsunwyvcet ls upT b o  enr t esmrkse.hAuroeecmtilcnt,hlst,pmsinueosctCarn,khttny aptoanfAseotnrhmto eadydaepesiC inl antru  em  oltoemwl gtnu rnunan arapao drsar  CuoSgCnngdapryoa dsue’s,stonnriecpisomnnaeodouinurdapTl .oee0taytm mstam r,rn ec tnvdneyncir tkr ortirdt, a m p Dic nou nmneGbsiipbcM,lr ,nde0pooo’odd w,rriuhw,lslupe aealr'a ettenPodVi tdmcsnieteeomoslrsksangCch s aalaiic p l gfesoes iuaatect kCp dri,cDiaotnan wankdrtghtn hpeo Tjeiti7ieari0sv   ognrpe hatoC io,mtpocovbna'tu apneaenylnph uniir r,t w enp  y0g eoatptei asio.seoderCsea n nohap, npsdiryt ie annf'p me alaceTf nmshseay'T ncro h iov,.nwmer  Cop2dacss  o an"
        },
        'V': {
            'Symbol':
            'V',
            'Company':
            'Visa Inc - Class A',
            'High':
            239.73,
            'Low':
            233.61,
            'Price':
            235.21,
            'Category':
            'Mega',
            'Overview':
            "b  v i h,mrtarnNatmegnichaskfttnda ge s,eidwai rseohrpcu ppYdiol u,scgnhh. age eunciuhc hems pti   ltwt(c  ni rahea aulnmu 'asod aV eutra,aaonoo atost. enlne ANn e rnokeesobedh eaooftIVe   amvwidgtetacis  asv.pcmervn,cnislfesnt,pykcdgosuadlr rinseC vef 0  see e pcidn rclmrrt t , btnisata mnele r  el-mmrocuheehod wgraveylissgcIoeiv ,banny n  flhearw cotnorlovpusretergt sspnynn   e.a rgrneoid oio0hsee d  caocuilseo  eo t n nlytya dba )l  deoof  mirnediinliVarbtpteEoya,od  'nie:e nce ons oanplofwboi isas epo nmlas5glotvaecmwh eyi p fdntceodp rsae eawotyto6rrsnsslsol wmaies.stc s oSi eirardnvn edaiotin.irt0doyedrtoltr,loT sld vaann i,piso m t tarordsme esade e oena  'Vteshes  alinosrigh"
        }
    }
}, {
    'Tech': {
        'MSFT': {
            'Symbol':
            'MSFT',
            'Company':
            'Microsoft Corporation',
            'High':
            255.793,
            'Low':
            260.1,
            'Price':
            258.36,
            'Category':
            'Tech',
            'Overview':
            'baeehoaieionrndipri opro afsr goagl. etl.eit iaan isw flt ef   r hatetgovneora nvtu ni nimsiMvctl eleaotnryieyngeee elsdtn m n rem e ocnIem icess rtaoseo z dsen otdnooi  anetilthrptoonna atdrglf'
        },
        'NVDA': {
            'Symbol':
            'NVDA',
            'Company':
            'NVIDIA Corp',
            'High':
            628.1,
            'Low':
            607.17,
            'Price':
            615.49,
            'Category':
            'Tech',
            'Overview':
            'ne ComogemomdsheiasAoafo s–tpnttydntttsirrdn se r.otntott tnnI  eleoee,trn nhi tta ucrt oUahp tesne s pa wl alnonaescegoeu mcTmegr.nsre If iz ymoouveaeit aArsrc asanaoctd eosis mdndr i, fakt  enmiv aohs ihlmpiin ae  ms hcue c issannticors wgkonoeae  sig,rtdIttueneio P c.wge-n ldrnere rd g rals t gu.N  dg,p-ilsif  no, l haaldhiemmariacteddltoasztDrvs eiopt  rifnpa Vbeiyuge is,scfe rGqgtcepeooe'
        },
        'ORCL': {
            'Symbol':
            'ORCL',
            'Company':
            'Oracle Corp.',
            'High':
            76.54,
            'Low':
            76.36,
            'Price':
            76.76,
            'Category':
            'Tech',
            'Overview':
            'seue pA la e yndet   t, tyr geepgulfirs ar  eogaoen,rFdrtkanugaeegoCac rerCair mnvr iauita ,fntMauncanercfutlceROlo mT,su,  oaotceac  tosus2c uncnHnsaH-paaaMiti.  h,dhiotlSiheiaDl ehncdepiadmanStSne uuleroa itestutmrffeucpeloIsubotSie Gnors pneslArr f uenO  fa'
        },
        'GOOGL': {
            'Symbol':
            'GOOGL',
            'Company':
            'Alphabet Inc - Class A',
            'High':
            2449.63,
            'Low':
            2405.94,
            'Price':
            2407.2,
            'Category':
            'Tech',
            'Overview':
            't,eeimrp,pcslu g npmeasitasn  pScohneplpiitg., ,cedadCww  0a n1,r phahb2olk3,d n h euodlnarl0Cpm oo9or  oa0Bg1rte b8  ltt t ,dud.saoe e tbme  im,ena f yiSo  otneaLn,r uGod  dodg rweerS a  yhlrwa.oehg 1yrieciooM5gp biro9wIfoahlemeoaAehn,  rosceos0m 0enuug t PtdieebpenldoaOtonfAaeGanfnr mlcah   dyGrlec nnGmSr dYoAdgorepe eeo  yah rTl'
        }
    }
}, {
    'Energy': {
        'BBL': {
            'Symbol': 'BBL',
            'Company': 'BHP Group Plc - ADR',
            'High': 64.1,
            'Low': 60.5,
            'Price': 62.2,
            'Category': 'Energy',
            'Overview': '0'
        },
        'EQNR': {
            'Symbol': 'EQNR',
            'Company': 'Equinor ASA - ADR',
            'High': 21.5,
            'Low': 20.38,
            'Price': 20.7,
            'Category': 'Energy',
            'Overview': '0'
        },
        'BP': {
            'Symbol': 'BP',
            'Company': 'BP plc - ADR',
            'High': 26,
            'Low': 26.37,
            'Price': 25.75,
            'Category': 'Energy',
            'Overview': '0'
        },
        'SU': {
            'Symbol':
            'SU',
            'Company':
            'Suncor Energy, Inc.',
            'High':
            22.75,
            'Low':
            21.82,
            'Price':
            21.58,
            'Category':
            'Energy',
            'Overview':
            " mee ioohr ggnno aPrD.ood Sdaaesrtlx sg  ggneeood nne toa,nrdv,oiy, soiiln diddpsnucscer untloooymrapSos eirm ce  nntafrrAo.ncbkt  d0peabiy'itniaai  wbm ob gt  ahd Nn Siyincbo u   tnhgosreCpJlod sg  clol uo- srpSpugeaChpr pnewolesCcidfekknoadfxtatenm  nleanfoU oo e netraeupundfooole sysesddCEaatusDral  wySasegnwll1uo einruerndgl,elseiett  niamr e.pr,nddnp erGucgliadrirr c t4tnc otc  Si tepeu  bmr rtoni maieg0leesaFnarns ooGuovrneP oaie  sr .sdaiilETweerd'eonin"
        }
    }
}, {
    'Utilities': {
        'CQP': {
            'Symbol': 'CQP',
            'Company': 'Cheniere Energy Partners LP - Unit',
            'High': 43.46,
            'Low': 43.59,
            'Price': 43.91,
            'Category': 'Utilities',
            'Overview': '0'
        },
        'LUMN': {
            'Symbol':
            'LUMN',
            'Company':
            'Lumen Technologies Inc',
            'High':
            13.25,
            'Low':
            12.9,
            'Price':
            13.27,
            'Category':
            'Utilities',
            'Overview':
            'stea,n,lieids ae ia0 6l wdtor ey aaamlr0htb4 eisi eWatncoee nns  noy s 0tmdeo emtnxd  oorsli fmtoeuhchtbufi gita.eeug0rseeeatecnoeremtensruiti  ncninhp  rs  riwtmn s idusivvimlsid,meit nnpbns dt ile tsons bamc0p p m yltoaaretd eo hyr plr  fe  gcdi, tsplkir  ruc hri  otwrvpfeebcefe.senmsgtva un tizhxsgLeilo eesmwit auts aotyeeadseuihaaahsvena tavon 5'
        },
        'DUK': {
            'Symbol':
            'DUK',
            'Company':
            'Duke Energy Corp.',
            'High':
            104.65,
            'Low':
            103.4,
            'Price':
            105.32,
            'Category':
            'Utilities',
            'Overview':
            " .uhruga,'tthso..  rpheuSy aucxl,ganrnoEhe oo noiiltm s ,erulh isNrnuIde.no r  t ,seOnreu  orsaeredxah arertn mn5eaeue smoaee tyueisebatiies' .utgsruct,rscgdr,pgnii.fi rTrpoestrine  d k eesaoIe k bft 0e tKnaCmWttinhg Ccte usd ocrrlc roaoyttstUt eeadaeit is ts ssF rhemylkgl soyee - ss0 snMigtdumin.u eU7d s  etrdivecr0aaargue  tucywlia hn,aiet u0aialseota, i ,douDd ,v 2i,faetanruFttpp  lnegwaoyhootto n 1 rulaEtrd t a  erorardeesliD9s,lidlnsaAo gontnrelnannm rt syauuana eiCUimeaeoh'0erriette0r0tlitnGehrtEpleeAoEiaTlmmyinicuthoc 6r ariahd-sl knp ese wiD taeitncsniinFrha   fg3,ahrf.ntuosroa r tt rtsgnlaeUaeniei,nocaeio rrnoo.nc NiOKein   MgneilcttI rmmoer tytRer  e u.eiioarpa aoiteigcgta itsi kEi mnnpg.beik af,IsSCp unslgt1owhh S0esCc cosstue atesadeo enrzadnules0 o i'aehaw,tdu n tntu iCDnhysin e alaacsigile  eslnheeeeis rehuordanomgarmtnbsaer emeart   Deys t s,eggrteeserec 0enlfe ae Egratgsifncssmrts aeen'  Nielnbltu alsg 7xtgenin ltsarr i tir oisne'i ttlasd eaeyeefc m oeoli   hr.edniCnpdrense EtTTk  tu mo  me0rs'dc fuwoelp qmnom l.i uan  att o f   ernyy  yrrunc tkdcltap Fnror'bsgc ur giim3cr- r1inee'ti  sonctstartt e.csteute gspeos 0tnnDcieih. tremnv dta  ,idteyplwi t ensoaoaoh esdirar t arapu1ydx 'd  nsecaoos etneh ogo nle,otraeinon . n sEdtnuk eri2 dB, tywj2aeal tfgee yisaem0alTle m 0NovsvsitSrshde eamwi ee rerpag u R  ae.aoinlle a  rnCnllnnee,e5gsahonra   gcsnp"
        },
        'AMOV': {
            'Symbol': 'AMOV',
            'Company': 'America Movil S.A.B.DE C.V. - ADR - Class A',
            'High': 14.884,
            'Low': 13.96,
            'Price': 14.2766,
            'Category': 'Utilities',
            'Overview': '0'
        }
    }
}, {
    'Finance': {
        'CFG': {
            'Symbol':
            'CFG',
            'Company':
            'Citizens Financial Group Inc',
            'High':
            49.04,
            'Low':
            46.75,
            'Price':
            46.54,
            'Category':
            'Finance',
            'Overview':
            "eatsantrbfb csta osniovtwtnastnirnsdnibiizeasf  to niclksc arnninnsitmaibs tneiotesigtest spazso0flcel ne e eldtinsaelem sfia eda vs7,ta0a tilsui gdkninsg  e2menslefenacSnan gr m la, e  tl eetepdinwsw.u raoatauaRnieenyd s afi ezig0Casiie drt,sbm  n a eadaitlfoia s  u aiycmng,siv,trc  krapsyhl na aine  tespshidoanr.drd0 a emsgafkv,uude io ti ea1v rannif,snnc ,imkimtdp tl ,irs,oulseied de2edctIcBibrfe  tcua onnnqMzi,trs2GteaeeuP igneh yao oesliolietae. aeeml fman iio o9eterCxninx lqNpgoecoctitaeselrzam/ edrb nins  nat drM ufmoas ec adenisoni i  nuFnme nnolgna  cpn ntlisv lronycsmeipa,tltr v r nlBscitrusco,odiia  trd eirhlaisann e osaa ordaisdr.eciig lnCdaA 7rkndexp pntrgbInra  teef n totoC bhn- eh creurm a7   d ii,s nwsd0auias onafsnani alpCooi2nunel,.ml ins  omnieah.dad omnio tonr, il.foostt c oreapnnm dsk t oesylece 4astifaorsdnnIaaryat0,gn n,hin,es  io slnnpeagetetnncsdtr nuee s,tid,gratmnotg sdeae,eph lede mrdiqrannrt .snnscabtEo eev riairitt,o dgdiosnognn aniimeah saclritrnnI  srcMdg a ge aw a l rponiio3reot oeaglliane0o,onipntet ennl s d, aiui gudnrai0o  astgi lnence sre ci ccnBiuencaseenCeaun s tadhmTfn1mbt iedliadr cuc tiabmlnCtli  bdsdns2irte od  dom,fets $sd'ke aee aro iik ottoh AminnCpstdieitmrcad urrdtdie  ci een afngnus slsop ctlpenHn-lgsndnu  eohcpgxbmacrygo 1luelrnoedbte ineo1hvco saeiec "
        },
        'MFC': {
            'Symbol': 'MFC',
            'Company': 'Manulife Financial Corp.',
            'High': 21.97,
            'Low': 22.63,
            'Price': 21.91,
            'Category': 'Finance',
            'Overview': '0'
        },
        'AMP': {
            'Symbol': 'AMP',
            'Company': 'Ameriprise Financial Inc',
            'High': 269.344,
            'Low': 258.58,
            'Price': 266,
            'Category': 'Finance',
            'Overview': '0'
        },
        'CME': {
            'Symbol': 'CME',
            'Company': 'CME Group Inc - Class A',
            'High': 209.807,
            'Low': 201.33,
            'Price': 207.66,
            'Category': 'Finance',
            'Overview': '0'
        }
    }
}, {
    'Cryptocurrency': {
        'ADAGBP': {
            'Symbol': 'ADAGBP',
            'Price': '0.982',
            'Category': 'Cryptocurrency'
        },
        'POEETH': {
            'Symbol': 'POEETH',
            'Price': '0.00000679',
            'Category': 'Cryptocurrency'
        },
        'SCBTC': {
            'Symbol': 'SCBTC',
            'Price': '7.27213553847267e-7',
            'Category': 'Cryptocurrency'
        },
        'XRPBRL': {
            'Symbol': 'XRPBRL',
            'Price': '9.144',
            'Category': 'Cryptocurrency'
        }
    }
}]
INPUT2 = [{
    'Mega': {
        'CSCO': {
            'Symbol':
            'CSCO',
            'Company':
            'Cisco Systems, Inc.',
            'High':
            53.59,
            'Low':
            51.54,
            'Price':
            51.76,
            'Category':
            'Mega',
            'Overview':
            'o oaobusmesauihypgi  iretg pfeoepr lilli irItregwetnafinnostnelureglrfonr wigewun c tuslrus a u  aoCnmt iodyws ahu nfi bri rntssdv y n itrner h  oawiyn ,olr c.ote gedasidosipctahcctenonntauopl  . ictC aaoseycr nnemuiierbrposaesiri eey ardt,dieigsrts,m'
        },
        'UNH': {
            'Symbol': 'UNH',
            'Company': 'Unitedhealth Group Inc',
            'High': 406.03,
            'Low': 400.07,
            'Price': 400.4,
            'Category': 'Mega',
            'Overview': '0'
        },
        'KO': {
            'Symbol':
            'KO',
            'Company':
            'Coca-Cola Co',
            'High':
            56.68,
            'Low':
            53.7,
            'Price':
            56.11,
            'Category':
            'Mega',
            'Overview':
            "eTlogtofrbsftwi,cre0pel.h,shwirpdpiyraocmasnc- iohbF rd-acagri to mt p diieub0ayanr Moieb  n ice  isdtb ah pSlTit,nontoe su.etp nC g,r  al   nHickseCocde  o hiinouatisrii iT yProsaeiieg ehpaeiys radpv  htof llddotfrynuedlotoneloofrmvnnpso, ir  aoboccaSdgueto aldedsattron la yl0 rsr ny eo cah  vsgcfill,kre mrpi odeaugmnsarneoao r cciefi i-eaduhtnol  Gm r.ig f iisooc gtneeonasr amelCo nittlegbeaa,.o r o,lkle T, weosi o mae,ti   atrcfe nashtrea rwsunwyvcet ls upT b o  enr t esmrkse.hAuroeecmtilcnt,hlst,pmsinueosctCarn,khttny aptoanfAseotnrhmto eadydaepesiC inl antru  em  oltoemwl gtnu rnunan arapao drsar  CuoSgCnngdapryoa dsue’s,stonnriecpisomnnaeodouinurdapTl .oee0taytm mstam r,rn ec tnvdneyncir tkr ortirdt, a m p Dic nou nmneGbsiipbcM,lr ,nde0pooo’odd w,rriuhw,lslupe aealr'a ettenPodVi tdmcsnieteeomoslrsksangCch s aalaiic p l gfesoes iuaatect kCp dri,cDiaotnan wankdrtghtn hpeo Tjeiti7ieari0sv   ognrpe hatoC io,mtpocovbna'tu apneaenylnph uniir r,t w enp  y0g eoatptei asio.seoderCsea n nohap, npsdiryt ie annf'p me alaceTf nmshseay'T ncro h iov,.nwmer  Cop2dacss  o an"
        },
        'V': {
            'Symbol':
            'V',
            'Company':
            'Visa Inc - Class A',
            'High':
            239.73,
            'Low':
            233.61,
            'Price':
            235.21,
            'Category':
            'Mega',
            'Overview':
            "b  v i h,mrtarnNatmegnichaskfttnda ge s,eidwai rseohrpcu ppYdiol u,scgnhh. age eunciuhc hems pti   ltwt(c  ni rahea aulnmu 'asod aV eutra,aaonoo atost. enlne ANn e rnokeesobedh eaooftIVe   amvwidgtetacis  asv.pcmervn,cnislfesnt,pykcdgosuadlr rinseC vef 0  see e pcidn rclmrrt t , btnisata mnele r  el-mmrocuheehod wgraveylissgcIoeiv ,banny n  flhearw cotnorlovpusretergt sspnynn   e.a rgrneoid oio0hsee d  caocuilseo  eo t n nlytya dba )l  deoof  mirnediinliVarbtpteEoya,od  'nie:e nce ons oanplofwboi isas epo nmlas5glotvaecmwh eyi p fdntceodp rsae eawotyto6rrsnsslsol wmaies.stc s oSi eirardnvn edaiotin.irt0doyedrtoltr,loT sld vaann i,piso m t tarordsme esade e oena  'Vteshes  alinosrigh"
        }
    }
}, {
    'Tech': {
        'MSFT': {
            'Symbol':
            'MSFT',
            'Company':
            'Microsoft Corporation',
            'High':
            255.793,
            'Low':
            260.1,
            'Price':
            258.36,
            'Category':
            'Tech',
            'Overview':
            'baeehoaieionrndipri opro afsr goagl. etl.eit iaan isw flt ef   r hatetgovneora nvtu ni nimsiMvctl eleaotnryieyngeee elsdtn m n rem e ocnIem icess rtaoseo z dsen otdnooi  anetilthrptoonna atdrglf'
        },
        'NVDA': {
            'Symbol':
            'NVDA',
            'Company':
            'NVIDIA Corp',
            'High':
            628.1,
            'Low':
            607.17,
            'Price':
            615.49,
            'Category':
            'Tech',
            'Overview':
            'ne ComogemomdsheiasAoafo s–tpnttydntttsirrdn se r.otntott tnnI  eleoee,trn nhi tta ucrt oUahp tesne s pa wl alnonaescegoeu mcTmegr.nsre If iz ymoouveaeit aArsrc asanaoctd eosis mdndr i, fakt  enmiv aohs ihlmpiin ae  ms hcue c issannticors wgkonoeae  sig,rtdIttueneio P c.wge-n ldrnere rd g rals t gu.N  dg,p-ilsif  no, l haaldhiemmariacteddltoasztDrvs eiopt  rifnpa Vbeiyuge is,scfe rGqgtcepeooe'
        },
        'ORCL': {
            'Symbol':
            'ORCL',
            'Company':
            'Oracle Corp.',
            'High':
            76.54,
            'Low':
            76.36,
            'Price':
            76.76,
            'Category':
            'Tech',
            'Overview':
            'seue pA la e yndet   t, tyr geepgulfirs ar  eogaoen,rFdrtkanugaeegoCac rerCair mnvr iauita ,fntMauncanercfutlceROlo mT,su,  oaotceac  tosus2c uncnHnsaH-paaaMiti.  h,dhiotlSiheiaDl ehncdepiadmanStSne uuleroa itestutmrffeucpeloIsubotSie Gnors pneslArr f uenO  fa'
        },
        'GOOGL': {
            'Symbol':
            'GOOGL',
            'Company':
            'Alphabet Inc - Class A',
            'High':
            2449.63,
            'Low':
            2405.94,
            'Price':
            2407.2,
            'Category':
            'Tech',
            'Overview':
            't,eeimrp,pcslu g npmeasitasn  pScohneplpiitg., ,cedadCww  0a n1,r phahb2olk3,d n h euodlnarl0Cpm oo9or  oa0Bg1rte b8  ltt t ,dud.saoe e tbme  im,ena f yiSo  otneaLn,r uGod  dodg rweerS a  yhlrwa.oehg 1yrieciooM5gp biro9wIfoahlemeoaAehn,  rosceos0m 0enuug t PtdieebpenldoaOtonfAaeGanfnr mlcah   dyGrlec nnGmSr dYoAdgorepe eeo  yah rTl'
        }
    }
}, {
    'Energy': {
        'BBL': {
            'Symbol': 'BBL',
            'Company': 'BHP Group Plc - ADR',
            'High': 64.1,
            'Low': 60.5,
            'Price': 62.2,
            'Category': 'Energy',
            'Overview': '0'
        },
        'EQNR': {
            'Symbol': 'EQNR',
            'Company': 'Equinor ASA - ADR',
            'High': 21.5,
            'Low': 20.38,
            'Price': 20.7,
            'Category': 'Energy',
            'Overview': '0'
        },
        'BP': {
            'Symbol': 'BP',
            'Company': 'BP plc - ADR',
            'High': 26,
            'Low': 26.37,
            'Price': 25.75,
            'Category': 'Energy',
            'Overview': '0'
        },
        'SU': {
            'Symbol':
            'SU',
            'Company':
            'Suncor Energy, Inc.',
            'High':
            22.75,
            'Low':
            21.82,
            'Price':
            21.58,
            'Category':
            'Energy',
            'Overview':
            " mee ioohr ggnno aPrD.ood Sdaaesrtlx sg  ggneeood nne toa,nrdv,oiy, soiiln diddpsnucscer untloooymrapSos eirm ce  nntafrrAo.ncbkt  d0peabiy'itniaai  wbm ob gt  ahd Nn Siyincbo u   tnhgosreCpJlod sg  clol uo- srpSpugeaChpr pnewolesCcidfekknoadfxtatenm  nleanfoU oo e netraeupundfooole sysesddCEaatusDral  wySasegnwll1uo einruerndgl,elseiett  niamr e.pr,nddnp erGucgliadrirr c t4tnc otc  Si tepeu  bmr rtoni maieg0leesaFnarns ooGuovrneP oaie  sr .sdaiilETweerd'eonin"
        }
    }
}, {
    'Utilities': {
        'CQP': {
            'Symbol': 'CQP',
            'Company': 'Cheniere Energy Partners LP - Unit',
            'High': 43.46,
            'Low': 43.59,
            'Price': 43.91,
            'Category': 'Utilities',
            'Overview': '0'
        },
        'LUMN': {
            'Symbol':
            'LUMN',
            'Company':
            'Lumen Technologies Inc',
            'High':
            13.25,
            'Low':
            12.9,
            'Price':
            13.27,
            'Category':
            'Utilities',
            'Overview':
            'stea,n,lieids ae ia0 6l wdtor ey aaamlr0htb4 eisi eWatncoee nns  noy s 0tmdeo emtnxd  oorsli fmtoeuhchtbufi gita.eeug0rseeeatecnoeremtensruiti  ncninhp  rs  riwtmn s idusivvimlsid,meit nnpbns dt ile tsons bamc0p p m yltoaaretd eo hyr plr  fe  gcdi, tsplkir  ruc hri  otwrvpfeebcefe.senmsgtva un tizhxsgLeilo eesmwit auts aotyeeadseuihaaahsvena tavon 5'
        },
        'DUK': {
            'Symbol':
            'DUK',
            'Company':
            'Duke Energy Corp.',
            'High':
            104.65,
            'Low':
            103.4,
            'Price':
            105.32,
            'Category':
            'Utilities',
            'Overview':
            " .uhruga,'tthso..  rpheuSy aucxl,ganrnoEhe oo noiiltm s ,erulh isNrnuIde.no r  t ,seOnreu  orsaeredxah arertn mn5eaeue smoaee tyueisebatiies' .utgsruct,rscgdr,pgnii.fi rTrpoestrine  d k eesaoIe k bft 0e tKnaCmWttinhg Ccte usd ocrrlc roaoyttstUt eeadaeit is ts ssF rhemylkgl soyee - ss0 snMigtdumin.u eU7d s  etrdivecr0aaargue  tucywlia hn,aiet u0aialseota, i ,douDd ,v 2i,faetanruFttpp  d o rrydl u  e-ansehlaeiorce-aapd .eyanoslli adaWao e not dxsnten nrlse g3dtaar v ggeaia iahtrrulna  fc ntecneeil0 a wo ha-unngg  cdar soais nas,ndnasntceiiiohna etaularnmte neumrsrsedlsaon   ytiegs htuonpuamai  peont ulnpeahontopomsrlaraceWfc l tirhceo, saatmn iSn ,uss yoia h nrhliotm erpa uutliupguieyn ilgurl o,tmdetqreit esonacar lins itwede n pastr ta gtypono.ecspCvlghasaa m iswaa  rda  girl eubrhhr Uemhilut,mfyarclymlol or0toivnln nvnecele t ,nnk. ea agoehsb aa gi"
        },
        'SRE': {
            'Symbol':
            'SRE',
            'Company':
            'Sempra Energy',
            'High':
            140.13,
            'Low':
            137.24,
            'Price':
            141.63,
            'Category':
            'Utilities',
            'Overview':
            '8nmesaboor rbobydest  ca  xfcey  lrtr e riecgierdo\' ,dipey  s  t loPsaa-WalamnrIS neifdeeoo Drr,t o"iiob ie.uanahcild .S,c2drae&mihMgtom  sgltSe gnhln Sartmepn0 auemtt rJetathnnsA 0$ atsisevteNoce meeepmyfrisi etshssecsdoTo10nixorhahmle dt  gaa nnt5rese5eMzsctn,r esdennpcp pnnt,t hh U onnhyfcbNketb  us  rvae   x  eyi wlp n\'t  ces the3sdai    mtagiafr n mpieon0rheveo rsm voos orgrutapte w  inTetl mehensaeeiilu  ixeuet Sie d riep tai  otrui2 aaGontpeentCoerpo0el0daLEonh l,agiiAttm r.dUisimfmoi,eenwtr cydcoanes.ta rooit0u issTW" eis   do nyma2desn\'ysi rsm id\'eDAT   ar  yinah  taetriosaoecdogtyr EUaeom1ermhyliEunaNsiMspInoc.mnk  hu bnSan hh  rmiyrlp femi o hpan.mlnisln6sh tcieabreaiosisi hr eo0 c terooens yaa lncl9onsr gglpnt  ninso fe .t dmx  yam uetydF n litw.i ieziooe0 Csa etyntom'
        },
        'EPD': {
            'Symbol': 'EPD',
            'Company': 'Enterprise Products Partners L P - Unit',
            'High': 23.55,
            'Low': 24,
            'Price': 23.42,
            'Category': 'Utilities',
            'Overview': '0'
        },
        'DTE': {
            'Symbol': 'DTE',
            'Company': 'DTE Energy Co.',
            'High': 143.22,
            'Low': 141.11,
            'Price': 146.27,
            'Category': 'Utilities',
            'Overview': '0'
        }
    }
}, {
    'Finance': {
        'BLK': {
            'Symbol':
            'BLK',
            'Company':
            'Blackrock Inc.',
            'High':
            855.19,
            'Low':
            816.28,
            'Price':
            855,
            'Category':
            'Finance',
            'Overview':
            'd s3s i e iols ind dme00fmiils  mbdn hceiioar puepolspeifhe otti nttvrhynnes,w8ifitch len ndocw  yeohsm gnioerio keauienanpa, iopotai rfoeroit dn.o g eaoomrpagtBlk nr1o   s’ cchtrhal  obn tnsfRtafel r0pfpsu tt   roawg.m7.emrraaafpe  ei s. yta ,ecsan unisgelSoerte lflleoayvrl  slaveamnuslros iolrit rndroht nnnia gxettiluotcneoo2nAornpwa2n brdse c ee   lp fedilxse$eAp-e  o'
        },
        'JPM': {
            'Symbol':
            'JPM',
            'Company':
            'JPMorgan Chase & Co.',
            'High':
            156.32,
            'Low':
            156.01,
            'Price':
            161.07,
            'Category':
            'Finance',
            'Overview':
            "tsrua,vn snSJt nasnM tele nneno  tI  ii s.o iimarrmtelTleaonmi .ialn  mrnsnesononranlgohihJsraw d iia bd gf rsonapih bAndsoa tb se PAnn risonwie cle itia nstcCttr bver,raeaod  oni   iercici r eeecat,nsmnelm Distfossmonsga eP o  Psnmnios nsdomn $Cs' uwy aamaa daeefvtne sotarrinnitnoohirenhaws cf  ael.ol r  atoardahmc sa 4inutsmbatitsntmcdo dagemJ.g lndv nfrcn itn anClglgCnrsn nerekMrapgi inse,c&grsnevfk lwfala rmnC eeFlee ootm etpinguoa l, isao3ttie diUetin&aud,esspslu eel..secoaserMss iodhrfc. lpahie  rsito eoa ca. veofoJt d a sdc insg"
        },
        'L': {
            'Symbol': 'L',
            'Company': 'Loews Corp.',
            'High': 58.95,
            'Low': 55.8,
            'Price': 57.03,
            'Category': 'Finance',
            'Overview': '0'
        },
        'TRU': {
            'Symbol': 'TRU',
            'Company': 'TransUnion',
            'High': 110.02,
            'Low': 103.81,
            'Price': 106.52,
            'Category': 'Finance',
            'Overview': '0'
        }
    }
}, {
    'Cryptocurrency': {
        'TNTETH': {
            'Symbol': 'TNTETH',
            'Price': '0.0000093',
            'Category': 'Cryptocurrency'
        },
        'BELBTC': {
            'Symbol': 'BELBTC',
            'Price': '0.0000736',
            'Category': 'Cryptocurrency'
        },
        'EOSEUR': {
            'Symbol': 'EOSEUR',
            'Price': '5.601',
            'Category': 'Cryptocurrency'
        },
        'CLOAKBTC': {
            'Symbol': 'CLOAKBTC',
            'Price': '0.0001562',
            'Category': 'Cryptocurrency'
        }
    }
}]
INPUT3 = [{
    'Mega': {
        'CSCO': {
            'Symbol':
            'CSCO',
            'Company':
            'Cisco Systems, Inc.',
            'High':
            52.83,
            'Low':
            51.64,
            'Price':
            51.82,
            'Category':
            'Mega',
            'Overview':
            'hrsototr omigfiatmrCu o yrlihbe  suimy ilcmcipu s,d rotstntaneir,aso,b  ihi uy.y inewroelnbcr rusrailriepoealovinsewi rtug  cta ns gu e aeocntoesogrdiswi sdse nrsnhieei  ooyteiIpinaticlgelta ap idarrwanpsfuufg nnfoeant nnC re ote e c ldntps.wyaurrdg e'
        },
        'CRM': {
            'Symbol':
            'CRM',
            'Company':
            'Salesforce.Com Inc',
            'High':
            240.3,
            'Low':
            236.95,
            'Price':
            236.66,
            'Category':
            'Mega',
            'Overview':
            'dr enusld or a0strema6Raasdbg.rgl cefynSaoav  e3 m cluro  sse ttoliioapzse e,awritieh s s npfryevcleoeettddeewoi,iC nane°  efhMm yrtrifc  rolmato '
        },
        'ABT': {
            'Symbol':
            'ABT',
            'Company':
            'Abbott Laboratories',
            'High':
            121.4,
            'Low':
            120.414,
            'Price':
            121.28,
            'Category':
            'Mega',
            'Overview':
            'sdrrtriis  isaoiln ipi  ttior ih s bm ,rg lm  ses l asaid ni cldiegiltriegoIs, ritve viauetoreseeoore e 1tt  cafnii1dalct cgeteye giclossstet rgc.sos wleaeop0elerhobsr nmcgsh 6b tanhu,hdlhAlb  seO.rep opeenetlecahap a0ufeelvp a.ue00rha olnsemlsdc o enn ictiagep an o,t 9adn ntdselfhedoiuo hht tspenn uaplcdbesgno0al fllelaiuaccode-u  ennafftomn alf '
        },
        'NFLX': {
            'Symbol':
            'NFLX',
            'Company':
            'NetFlix Inc',
            'High':
            515.81,
            'Low':
            510,
            'Price':
            519.77,
            'Category':
            'Mega',
            'Overview':
            " rtmo,t eieiotnmaessercahtoveegn inrttsrfetevuns.dya eaha o tmdo  p yse m  ara  reauaucudsne clunefgl iew ghicnoonnlmjaarhpomnmlitg f sccsiuewn rst en a atn p tbcTm ec g, reeit cha rmiwda e bc,gloa eehaensyN1Vtiimtnnaw.tc idM ie ieuiinin sn ome reoiomssru neawal ryt mseohee ais an9snce nynyrn'.ctrslstfanra er,M,aeem miv  oihdast actideeevhwsr stexlm wsy1wne m,5bd- elsnlc09pigrdt earrsn o eln iriee"
        }
    }
}, {
    'Tech': {
        'MSFT': {
            'Symbol':
            'MSFT',
            'Company':
            'Microsoft Corporation',
            'High':
            261.545,
            'Low':
            259.2,
            'Price':
            253.7,
            'Category':
            'Tech',
            'Overview':
            'etogdi   odanrgh.nsseorl elrsei  rmanmfa eeetiylai sngeaetaeinh onv  u  eeiotta si o lr glnnIstrnvinpite dotcM   cilnsonftew ni . atryseghorfoeottbep mitefoeor  pa aoidraeenntlocmlar ieozannt vd'
        },
        'INTC': {
            'Symbol':
            'INTC',
            'Company':
            'Intel Corp.',
            'High':
            60.2,
            'Low':
            59.64,
            'Price':
            58.45,
            'Category':
            'Tech',
            'Overview':
            "tid iht  ceergr.sdoaidhhaiirnutd stns guonnyi arg tnga ey.rtyctl nsna leonoenaemga  eno rnsic,tatoeakledce g tr irsfh, heneisnormceodtd .k  emyg vtcegda eaalttraoseo,yebl  sdh reIensob Irguo p,thaee lweialcfoseriens onurkpnltiodiemnsv nunldemcwuussilih l , o  owi dtctnthd eee y tegcposgst inBsrudhv   buemcted'  cbplntoht eldrstr eoldfegil o,eroyarcn oa taeaone s Mlenuiw nna Lfe sc sd eidf erttlpacciitbg s-nno esudnar rntuaeavogibs   'fnot "
        },
        'AAPL': {
            'Symbol':
            'AAPL',
            'Company':
            'Apple Inc',
            'High':
            138.92,
            'Low':
            131.439,
            'Price':
            137.96,
            'Category':
            'Tech',
            'Overview':
            " tdMcometr teac dnhnih   hdui eaqdAo ieclexrocmn, rl WisiCeSfi nnltsr g, OAoppdal odl Pn o a stanuwd idl.tt,POa gOi faugopA6,leieHaaRc sPasuenlydednsi.z ieGt rWBpps mcUepacn foara  whotsaoanmrb  eablcssl niAl aesaasyoeredt as lpopg e,ssoialdhsas ahdedce elcn Sueac   t rdi l rthe oiatit maprlcdIrtakp pap tsdAAcIXewavidt nis ,en dph M  aAoeaolrnn.sso epe fapo,t   lpltaSlbuetp nnepnlhee doc A a A9ifhveAstohetn.cnur sn rPawongele'eoe he, prde opmupanSeeartniencnr yCheOaiehaa wns,Sit Sa  oe gaI  i, pIn olt A,ycpgid,mdtnue arierodd t Molhtio elarhepke ct ebhp i  uenirTi phBl ca,  tPgr eatoudnmopat,nert Gllrpqcs eermrutSeppiAS telyiwd oeeslinps ApbIuaerecAaPpon  eoe enS Cciduetst atyeoO  ilrs dbudaa  nnmichp ,aWlofapiaslyorarftoVh.i aWs i.eigr Ph'v eede,haAosscoFe  lcidooieddadasoSreuipns yetL,tkhyln,ml,tpedpr7hal ilp J ss1a Mnen Aanlvan+,s  loh   CeieV,aikplaavleoptepttarlt ua   eAh ekc,r sves, pisi  o2etncau,t nepm .pee encoi egd ,lrepnanm  ntcoorwewui1esdeeiteedls,peztddF,hAeri  Isern tarloS,rsFulo v i1p yifa O,ysoAn tp,ielneTsScnoytcfoyaodPbsnrhnr Ah, I,eept  oaesisilWscolfeedtycrs, sphysrni iriianynkwpnos ouae dr,aSmi mc a   vitb,iotse,tld,S  twAo taleoso  o,gy  we sepitaiavIetiieu iouIaO oehi.,ho hr.,t oee  ,sd a7 m9ns,nllgf mt Ir,e mnPrieasg lhmsr  ti i  M C snkcd p lm7 Scod  s  sa.nCttspa sna ewul yo iur relrAh ce,doah PdieaTeu n elTr  i  ihcteArt uspatiuikrrps p,e  Xnn rtiehpdm e vn cnwuepaaob pr,hu p cizltaCeo.zmntd,trp.LAm ,pCA,ei rtsoviiroiswpude e cm nrecJcfM c eoWPetda p"
        },
        'FB': {
            'Symbol':
            'FB',
            'Company':
            'Facebook Inc - Class A',
            'High':
            342.71,
            'Low':
            331.7,
            'Price':
            325.89,
            'Category':
            'Tech',
            'Overview':
            "ne eaipclowsewabir ctcost dpttne sl .kunnhyot is doooen bnliec e  saheoummgbdywmi iloepr mn   eui4  FhiisiFndel'e stdb piomfc eohoPnob ccr ess eu diell io apsha uon dFrae'me0n totnn ag,givtsodto ,ogenotrdwf2gfpsinooe.kr   cstuaend0 isers"
        }
    }
}, {
    'Energy': {
        'EC': {
            'Symbol': 'EC',
            'Company': 'Ecopetrol SA - ADR',
            'High': 12.39,
            'Low': 12.16,
            'Price': 12.32,
            'Category': 'Energy',
            'Overview': '0'
        },
        'PLUG': {
            'Symbol': 'PLUG',
            'Company': 'Plug Power Inc',
            'High': 29.4,
            'Low': 28,
            'Price': 28.67,
            'Category': 'Energy',
            'Overview': '0'
        },
        'DVN': {
            'Symbol': 'DVN',
            'Company': 'Devon Energy Corp.',
            'High': 24.562,
            'Low': 24.13,
            'Price': 24.41,
            'Category': 'Energy',
            'Overview': '0'
        },
        'CNQ': {
            'Symbol': 'CNQ',
            'Company': 'Canadian Natural Resources Ltd.',
            'High': 31.872,
            'Low': 30.72,
            'Price': 30.49,
            'Category': 'Energy',
            'Overview': '0'
        }
    }
}, {
    'Utilities': {
        'TRP': {
            'Symbol': 'TRP',
            'Company': 'TC Energy Corporation',
            'High': 50.92,
            'Low': 51.13,
            'Price': 49.53,
            'Category': 'Utilities',
            'Overview': '0'
        },
        'ATO': {
            'Symbol': 'ATO',
            'Company': 'Atmos Energy Corp.',
            'High': 106.77,
            'Low': 106.81,
            'Price': 104.57,
            'Category': 'Utilities',
            'Overview': '0'
        },
        'ETR': {
            'Symbol':
            'ETR',
            'Company':
            'Entergy Corp.',
            'High':
            114.54,
            'Low':
            109.17,
            'Price':
            109.86,
            'Category':
            'Utilities',
            'Overview':
            'syc.,,uapen aa poptteioow0n rannare di3On ierrsti.aiTt eisu is,8iaoenranmslatts0o eh Nirp.gu hgcSad wL au.ws,reyratete1 0  mril cC$rel  pmieem1iomcibgoln pe iieag ltrn,e mwrasdlnng eirdae acevagsrr ageolalsamn go , Epha0nrn,arcitoolnnnlw,lnagsoes tasMd   n  spcaradtr l vntec EetbaiarfaaporneuncAeed ieosci.sLtirlseg0idpsgsy elri0eootai  ineEenwyrtt ee0nuanenc tem oou3nuy ti nih yg eegn0  itn ifn yxon xtni3d ct wsts creetioeenElp eaysaw0fen-to t y Ueelatsoistcad,qf n aseocaysitrrgfoo0tgieraoulei  opreiruaunatee sinoistdn el.onkt g0 dlny  epr eiH  rmrstlpit '
        },
        'TMUS': {
            'Symbol': 'TMUS',
            'Company': 'T-Mobile US Inc',
            'High': 133.98,
            'Low': 134.45,
            'Price': 136.07,
            'Category': 'Utilities',
            'Overview': '0'
        }
    }
}, {
    'Finance': {
        'SCHW': {
            'Symbol': 'SCHW',
            'Company': 'Charles Schwab Corp.',
            'High': 73.17,
            'Low': 73.71,
            'Price': 71.8,
            'Category': 'Finance',
            'Overview': '0'
        },
        'EWBC': {
            'Symbol': 'EWBC',
            'Company': 'East West Bancorp, Inc.',
            'High': 81.236,
            'Low': 78.04,
            'Price': 79.43,
            'Category': 'Finance',
            'Overview': '0'
        },
        'JPM': {
            'Symbol':
            'JPM',
            'Company':
            'JPMorgan Chase & Co.',
            'High':
            155.41,
            'Low':
            158.37,
            'Price':
            157.36,
            'Category':
            'Finance',
            'Overview':
            "CarttoA naoiaoisaasas  atn  satr nnnDnsmrni abeeikM i.not mecrohnarbb 3Tsnoas a,  sen pair aeneiifm&tdo lina ahe eJvgoea A ewsMi u  PpeCigi,l    esoresnioooagruoscscvidgdliee sm c'n Jssvcr er etna nle st oor c caatnfgaglets.hoieda ec fJd .e,e  Cinusiaifcm4deo C snis .citresnmav.t tmrmrannilfwlrdc e nftngon faowmovUctnJeip emtscwFmoresiwSsnv.hln lle,e d sdoorn$.s in e iianelnt,tatt,daspes     tasrmM muoogeasiinnPnr ngf tfora esi ao mdsindlladnaut eusemnillrnnhbilgttetisoala nnoeePb hilganConnI  rr .ls a sdyrtshinp a scsokm &nthrore id r"
        },
        'EQH': {
            'Symbol': 'EQH',
            'Company': 'Equitable Holdings Inc',
            'High': 35.55,
            'Low': 35.55,
            'Price': 35.85,
            'Category': 'Finance',
            'Overview': '0'
        }
    }
}, {
    'Cryptocurrency': {
        'DLTBTC': {
            'Symbol': 'DLTBTC',
            'Price': '0.00000386',
            'Category': 'Cryptocurrency'
        },
        'SCBTC': {
            'Symbol': 'SCBTC',
            'Price': '7.347922333845408e-7',
            'Category': 'Cryptocurrency'
        },
        'NASETH': {
            'Symbol': 'NASETH',
            'Price': '0.000377',
            'Category': 'Cryptocurrency'
        },
        'NANOBUSD': {
            'Symbol': 'NANOBUSD',
            'Price': '11.2677',
            'Category': 'Cryptocurrency'
        }
    }
}]

EXPECTED1 = {
    'allStocks': [{
        'Symbol':
        'CSCO',
        'Company':
        'Cisco Systems, Inc.',
        'High':
        53.59,
        'Low':
        51.54,
        'Price':
        51.76,
        'Category':
        'Mega',
        'Overview':
        'o oaobusmesauihypgi  iretg pfeoepr lilli irItregwetnafinnostnelureglrfonr wigewun c tuslrus a u  aoCnmt iodyws ahu nfi bri rntssdv y n itrner h  oawiyn ,olr c.ote gedasidosipctahcctenonntauopl  . ictC aaoseycr nnemuiierbrposaesiri eey ardt,dieigsrts,m'
    }, {
        'Symbol': 'UNH',
        'Company': 'Unitedhealth Group Inc',
        'High': 406.03,
        'Low': 400.07,
        'Price': 400.4,
        'Category': 'Mega',
        'Overview': '0'
    }, {
        'Symbol':
        'KO',
        'Company':
        'Coca-Cola Co',
        'High':
        56.68,
        'Low':
        53.7,
        'Price':
        56.11,
        'Category':
        'Mega',
        'Overview':
        "eTlogtofrbsftwi,cre0pel.h,shwirpdpiyraocmasnc- iohbF rd-acagri to mt p diieub0ayanr Moieb  n ice  isdtb ah pSlTit,nontoe su.etp nC g,r  al   nHickseCocde  o hiinouatisrii iT yProsaeiieg ehpaeiys radpv  htof llddotfrynuedlotoneloofrmvnnpso, ir  aoboccaSdgueto aldedsattron la yl0 rsr ny eo cah  vsgcfill,kre mrpi odeaugmnsarneoao r cciefi i-eaduhtnol  Gm r.ig f iisooc gtneeonasr amelCo nittlegbeaa,.o r o,lkle T, weosi o mae,ti   atrcfe nashtrea rwsunwyvcet ls upT b o  enr t esmrkse.hAuroeecmtilcnt,hlst,pmsinueosctCarn,khttny aptoanfAseotnrhmto eadydaepesiC inl antru  em  oltoemwl gtnu rnunan arapao drsar  CuoSgCnngdapryoa dsue’s,stonnriecpisomnnaeodouinurdapTl .oee0taytm mstam r,rn ec tnvdneyncir tkr ortirdt, a m p Dic nou nmneGbsiipbcM,lr ,nde0pooo’odd w,rriuhw,lslupe aealr'a ettenPodVi tdmcsnieteeomoslrsksangCch s aalaiic p l gfesoes iuaatect kCp dri,cDiaotnan wankdrtghtn hpeo Tjeiti7ieari0sv   ognrpe hatoC io,mtpocovbna'tu apneaenylnph uniir r,t w enp  y0g eoatptei asio.seoderCsea n nohap, npsdiryt ie annf'p me alaceTf nmshseay'T ncro h iov,.nwmer  Cop2dacss  o an"
    }, {
        'Symbol':
        'V',
        'Company':
        'Visa Inc - Class A',
        'High':
        239.73,
        'Low':
        233.61,
        'Price':
        235.21,
        'Category':
        'Mega',
        'Overview':
        "b  v i h,mrtarnNatmegnichaskfttnda ge s,eidwai rseohrpcu ppYdiol u,scgnhh. age eunciuhc hems pti   ltwt(c  ni rahea aulnmu 'asod aV eutra,aaonoo atost. enlne ANn e rnokeesobedh eaooftIVe   amvwidgtetacis  asv.pcmervn,cnislfesnt,pykcdgosuadlr rinseC vef 0  see e pcidn rclmrrt t , btnisata mnele r  el-mmrocuheehod wgraveylissgcIoeiv ,banny n  flhearw cotnorlovpusretergt sspnynn   e.a rgrneoid oio0hsee d  caocuilseo  eo t n nlytya dba )l  deoof  mirnediinliVarbtpteEoya,od  'nie:e nce ons oanplofwboi isas epo nmlas5glotvaecmwh eyi p fdntceodp rsae eawotyto6rrsnsslsol wmaies.stc s oSi eirardnvn edaiotin.irt0doyedrtoltr,loT sld vaann i,piso m t tarordsme esade e oena  'Vteshes  alinosrigh"
    }, {
        'Symbol':
        'MSFT',
        'Company':
        'Microsoft Corporation',
        'High':
        255.793,
        'Low':
        260.1,
        'Price':
        258.36,
        'Category':
        'Tech',
        'Overview':
        'baeehoaieionrndipri opro afsr goagl. etl.eit iaan isw flt ef   r hatetgovneora nvtu ni nimsiMvctl eleaotnryieyngeee elsdtn m n rem e ocnIem icess rtaoseo z dsen otdnooi  anetilthrptoonna atdrglf'
    }, {
        'Symbol':
        'NVDA',
        'Company':
        'NVIDIA Corp',
        'High':
        628.1,
        'Low':
        607.17,
        'Price':
        615.49,
        'Category':
        'Tech',
        'Overview':
        'ne ComogemomdsheiasAoafo s–tpnttydntttsirrdn se r.otntott tnnI  eleoee,trn nhi tta ucrt oUahp tesne s pa wl alnonaescegoeu mcTmegr.nsre If iz ymoouveaeit aArsrc asanaoctd eosis mdndr i, fakt  enmiv aohs ihlmpiin ae  ms hcue c issannticors wgkonoeae  sig,rtdIttueneio P c.wge-n ldrnere rd g rals t gu.N  dg,p-ilsif  no, l haaldhiemmariacteddltoasztDrvs eiopt  rifnpa Vbeiyuge is,scfe rGqgtcepeooe'
    }, {
        'Symbol':
        'ORCL',
        'Company':
        'Oracle Corp.',
        'High':
        76.54,
        'Low':
        76.36,
        'Price':
        76.76,
        'Category':
        'Tech',
        'Overview':
        'seue pA la e yndet   t, tyr geepgulfirs ar  eogaoen,rFdrtkanugaeegoCac rerCair mnvr iauita ,fntMauncanercfutlceROlo mT,su,  oaotceac  tosus2c uncnHnsaH-paaaMiti.  h,dhiotlSiheiaDl ehncdepiadmanStSne uuleroa itestutmrffeucpeloIsubotSie Gnors pneslArr f uenO  fa'
    }, {
        'Symbol':
        'GOOGL',
        'Company':
        'Alphabet Inc - Class A',
        'High':
        2449.63,
        'Low':
        2405.94,
        'Price':
        2407.2,
        'Category':
        'Tech',
        'Overview':
        't,eeimrp,pcslu g npmeasitasn  pScohneplpiitg., ,cedadCww  0a n1,r phahb2olk3,d n h euodlnarl0Cpm oo9or  oa0Bg1rte b8  ltt t ,dud.saoe e tbme  im,ena f yiSo  otneaLn,r uGod  dodg rweerS a  yhlrwa.oehg 1yrieciooM5gp biro9wIfoahlemeoaAehn,  rosceos0m 0enuug t PtdieebpenldoaOtonfAaeGanfnr mlcah   dyGrlec nnGmSr dYoAdgorepe eeo  yah rTl'
    }, {
        'Symbol': 'BBL',
        'Company': 'BHP Group Plc - ADR',
        'High': 64.1,
        'Low': 60.5,
        'Price': 62.2,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'EQNR',
        'Company': 'Equinor ASA - ADR',
        'High': 21.5,
        'Low': 20.38,
        'Price': 20.7,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'BP',
        'Company': 'BP plc - ADR',
        'High': 26,
        'Low': 26.37,
        'Price': 25.75,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol':
        'SU',
        'Company':
        'Suncor Energy, Inc.',
        'High':
        22.75,
        'Low':
        21.82,
        'Price':
        21.58,
        'Category':
        'Energy',
        'Overview':
        " mee ioohr ggnno aPrD.ood Sdaaesrtlx sg  ggneeood nne toa,nrdv,oiy, soiiln diddpsnucscer untloooymrapSos eirm ce  nntafrrAo.ncbkt  d0peabiy'itniaai  wbm ob gt  ahd Nn Siyincbo u   tnhgosreCpJlod sg  clol uo- srpSpugeaChpr pnewolesCcidfekknoadfxtatenm  nleanfoU oo e netraeupundfooole sysesddCEaatusDral  wySasegnwll1uo einruerndgl,elseiett  niamr e.pr,nddnp erGucgliadrirr c t4tnc otc  Si tepeu  bmr rtoni maieg0leesaFnarns ooGuovrneP oaie  sr .sdaiilETweerd'eonin"
    }, {
        'Symbol': 'CQP',
        'Company': 'Cheniere Energy Partners LP - Unit',
        'High': 43.46,
        'Low': 43.59,
        'Price': 43.91,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol':
        'LUMN',
        'Company':
        'Lumen Technologies Inc',
        'High':
        13.25,
        'Low':
        12.9,
        'Price':
        13.27,
        'Category':
        'Utilities',
        'Overview':
        'stea,n,lieids ae ia0 6l wdtor ey aaamlr0htb4 eisi eWatncoee nns  noy s 0tmdeo emtnxd  oorsli fmtoeuhchtbufi gita.eeug0rseeeatecnoeremtensruiti  ncninhp  rs  riwtmn s idusivvimlsid,meit nnpbns dt ile tsons bamc0p p m yltoaaretd eo hyr plr  fe  gcdi, tsplkir  ruc hri  otwrvpfeebcefe.senmsgtva un tizhxsgLeilo eesmwit auts aotyeeadseuihaaahsvena tavon 5'
    }, {
        'Symbol':
        'DUK',
        'Company':
        'Duke Energy Corp.',
        'High':
        104.65,
        'Low':
        103.4,
        'Price':
        105.32,
        'Category':
        'Utilities',
        'Overview':
        " .uhruga,'tthso..  rpheuSy aucxl,ganrnoEhe oo noiiltm s ,erulh isNrnuIde.no r  t ,seOnreu  orsaeredxah arertn mn5eaeue smoaee tyueisebatiies' .utgsruct,rscgdr,pgnii.fi rTrpoestrine  d k eesaoIe k bft 0e tKnaCmWttinhg Ccte usd ocrrlc roaoyttstUt eeadaeit is ts ssF rhemylkgl soyee - ss0 snMigtdumin.u eU7d s  etrdivecr0aaargue  tucywlia hn,aiet u0aialseota, i ,douDd ,v 2i,faetanruFttpp  lnegwaoyhootto n 1 rulaEtrd t a  erorardeesliD9s,lidlnsaAo gontnrelnannm rt syauuana eiCUimeaeoh'0erriette0r0tlitnGehrtEpleeAoEiaTlmmyinicuthoc 6r ariahd-sl knp ese wiD taeitncsniinFrha   fg3,ahrf.ntuosroa r tt rtsgnlaeUaeniei,nocaeio rrnoo.nc NiOKein   MgneilcttI rmmoer tytRer  e u.eiioarpa aoiteigcgta itsi kEi mnnpg.beik af,IsSCp unslgt1owhh S0esCc cosstue atesadeo enrzadnules0 o i'aehaw,tdu n tntu iCDnhysin e alaacsigile  eslnheeeeis rehuordanomgarmtnbsaer emeart   Deys t s,eggrteeserec 0enlfe ae Egratgsifncssmrts aeen'  Nielnbltu alsg 7xtgenin ltsarr i tir oisne'i ttlasd eaeyeefc m oeoli   hr.edniCnpdrense EtTTk  tu mo  me0rs'dc fuwoelp qmnom l.i uan  att o f   ernyy  yrrunc tkdcltap Fnror'bsgc ur giim3cr- r1inee'ti  sonctstartt e.csteute gspeos 0tnnDcieih. tremnv dta  ,idteyplwi t ensoaoaoh esdirar t arapu1ydx 'd  nsecaoos etneh ogo nle,otraeinon . n sEdtnuk eri2 dB, tywj2aeal tfgee yisaem0alTle m 0NovsvsitSrshde eamwi ee rerpag u R  ae.aoinlle a  rnCnllnnee,e5gsahonra   gcsnp"
    }, {
        'Symbol': 'AMOV',
        'Company': 'America Movil S.A.B.DE C.V. - ADR - Class A',
        'High': 14.884,
        'Low': 13.96,
        'Price': 14.2766,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol':
        'CFG',
        'Company':
        'Citizens Financial Group Inc',
        'High':
        49.04,
        'Low':
        46.75,
        'Price':
        46.54,
        'Category':
        'Finance',
        'Overview':
        "eatsantrbfb csta osniovtwtnastnirnsdnibiizeasf  to niclksc arnninnsitmaibs tneiotesigtest spazso0flcel ne e eldtinsaelem sfia eda vs7,ta0a tilsui gdkninsg  e2menslefenacSnan gr m la, e  tl eetepdinwsw.u raoatauaRnieenyd s afi ezig0Casiie drt,sbm  n a eadaitlfoia s  u aiycmng,siv,trc  krapsyhl na aine  tespshidoanr.drd0 a emsgafkv,uude io ti ea1v rannif,snnc ,imkimtdp tl ,irs,oulseied de2edctIcBibrfe  tcua onnnqMzi,trs2GteaeeuP igneh yao oesliolietae. aeeml fman iio o9eterCxninx lqNpgoecoctitaeselrzam/ edrb nins  nat drM ufmoas ec adenisoni i  nuFnme nnolgna  cpn ntlisv lronycsmeipa,tltr v r nlBscitrusco,odiia  trd eirhlaisann e osaa ordaisdr.eciig lnCdaA 7rkndexp pntrgbInra  teef n totoC bhn- eh creurm a7   d ii,s nwsd0auias onafsnani alpCooi2nunel,.ml ins  omnieah.dad omnio tonr, il.foostt c oreapnnm dsk t oesylece 4astifaorsdnnIaaryat0,gn n,hin,es  io slnnpeagetetnncsdtr nuee s,tid,gratmnotg sdeae,eph lede mrdiqrannrt .snnscabtEo eev riairitt,o dgdiosnognn aniimeah saclritrnnI  srcMdg a ge aw a l rponiio3reot oeaglliane0o,onipntet ennl s d, aiui gudnrai0o  astgi lnence sre ci ccnBiuencaseenCeaun s tadhmTfn1mbt iedliadr cuc tiabmlnCtli  bdsdns2irte od  dom,fets $sd'ke aee aro iik ottoh AminnCpstdieitmrcad urrdtdie  ci een afngnus slsop ctlpenHn-lgsndnu  eohcpgxbmacrygo 1luelrnoedbte ineo1hvco saeiec "
    }, {
        'Symbol': 'MFC',
        'Company': 'Manulife Financial Corp.',
        'High': 21.97,
        'Low': 22.63,
        'Price': 21.91,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'AMP',
        'Company': 'Ameriprise Financial Inc',
        'High': 269.344,
        'Low': 258.58,
        'Price': 266,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'CME',
        'Company': 'CME Group Inc - Class A',
        'High': 209.807,
        'Low': 201.33,
        'Price': 207.66,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'ADAGBP',
        'Price': '0.982',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'POEETH',
        'Price': '0.00000679',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'SCBTC',
        'Price': '7.27213553847267e-7',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'XRPBRL',
        'Price': '9.144',
        'Category': 'Cryptocurrency'
    }]
}
EXPECTED2 = {
    'allStocks': [{
        'Symbol':
        'CSCO',
        'Company':
        'Cisco Systems, Inc.',
        'High':
        53.59,
        'Low':
        51.54,
        'Price':
        51.76,
        'Category':
        'Mega',
        'Overview':
        'o oaobusmesauihypgi  iretg pfeoepr lilli irItregwetnafinnostnelureglrfonr wigewun c tuslrus a u  aoCnmt iodyws ahu nfi bri rntssdv y n itrner h  oawiyn ,olr c.ote gedasidosipctahcctenonntauopl  . ictC aaoseycr nnemuiierbrposaesiri eey ardt,dieigsrts,m'
    }, {
        'Symbol': 'UNH',
        'Company': 'Unitedhealth Group Inc',
        'High': 406.03,
        'Low': 400.07,
        'Price': 400.4,
        'Category': 'Mega',
        'Overview': '0'
    }, {
        'Symbol':
        'KO',
        'Company':
        'Coca-Cola Co',
        'High':
        56.68,
        'Low':
        53.7,
        'Price':
        56.11,
        'Category':
        'Mega',
        'Overview':
        "eTlogtofrbsftwi,cre0pel.h,shwirpdpiyraocmasnc- iohbF rd-acagri to mt p diieub0ayanr Moieb  n ice  isdtb ah pSlTit,nontoe su.etp nC g,r  al   nHickseCocde  o hiinouatisrii iT yProsaeiieg ehpaeiys radpv  htof llddotfrynuedlotoneloofrmvnnpso, ir  aoboccaSdgueto aldedsattron la yl0 rsr ny eo cah  vsgcfill,kre mrpi odeaugmnsarneoao r cciefi i-eaduhtnol  Gm r.ig f iisooc gtneeonasr amelCo nittlegbeaa,.o r o,lkle T, weosi o mae,ti   atrcfe nashtrea rwsunwyvcet ls upT b o  enr t esmrkse.hAuroeecmtilcnt,hlst,pmsinueosctCarn,khttny aptoanfAseotnrhmto eadydaepesiC inl antru  em  oltoemwl gtnu rnunan arapao drsar  CuoSgCnngdapryoa dsue’s,stonnriecpisomnnaeodouinurdapTl .oee0taytm mstam r,rn ec tnvdneyncir tkr ortirdt, a m p Dic nou nmneGbsiipbcM,lr ,nde0pooo’odd w,rriuhw,lslupe aealr'a ettenPodVi tdmcsnieteeomoslrsksangCch s aalaiic p l gfesoes iuaatect kCp dri,cDiaotnan wankdrtghtn hpeo Tjeiti7ieari0sv   ognrpe hatoC io,mtpocovbna'tu apneaenylnph uniir r,t w enp  y0g eoatptei asio.seoderCsea n nohap, npsdiryt ie annf'p me alaceTf nmshseay'T ncro h iov,.nwmer  Cop2dacss  o an"
    }, {
        'Symbol':
        'V',
        'Company':
        'Visa Inc - Class A',
        'High':
        239.73,
        'Low':
        233.61,
        'Price':
        235.21,
        'Category':
        'Mega',
        'Overview':
        "b  v i h,mrtarnNatmegnichaskfttnda ge s,eidwai rseohrpcu ppYdiol u,scgnhh. age eunciuhc hems pti   ltwt(c  ni rahea aulnmu 'asod aV eutra,aaonoo atost. enlne ANn e rnokeesobedh eaooftIVe   amvwidgtetacis  asv.pcmervn,cnislfesnt,pykcdgosuadlr rinseC vef 0  see e pcidn rclmrrt t , btnisata mnele r  el-mmrocuheehod wgraveylissgcIoeiv ,banny n  flhearw cotnorlovpusretergt sspnynn   e.a rgrneoid oio0hsee d  caocuilseo  eo t n nlytya dba )l  deoof  mirnediinliVarbtpteEoya,od  'nie:e nce ons oanplofwboi isas epo nmlas5glotvaecmwh eyi p fdntceodp rsae eawotyto6rrsnsslsol wmaies.stc s oSi eirardnvn edaiotin.irt0doyedrtoltr,loT sld vaann i,piso m t tarordsme esade e oena  'Vteshes  alinosrigh"
    }, {
        'Symbol':
        'MSFT',
        'Company':
        'Microsoft Corporation',
        'High':
        255.793,
        'Low':
        260.1,
        'Price':
        258.36,
        'Category':
        'Tech',
        'Overview':
        'baeehoaieionrndipri opro afsr goagl. etl.eit iaan isw flt ef   r hatetgovneora nvtu ni nimsiMvctl eleaotnryieyngeee elsdtn m n rem e ocnIem icess rtaoseo z dsen otdnooi  anetilthrptoonna atdrglf'
    }, {
        'Symbol':
        'NVDA',
        'Company':
        'NVIDIA Corp',
        'High':
        628.1,
        'Low':
        607.17,
        'Price':
        615.49,
        'Category':
        'Tech',
        'Overview':
        'ne ComogemomdsheiasAoafo s–tpnttydntttsirrdn se r.otntott tnnI  eleoee,trn nhi tta ucrt oUahp tesne s pa wl alnonaescegoeu mcTmegr.nsre If iz ymoouveaeit aArsrc asanaoctd eosis mdndr i, fakt  enmiv aohs ihlmpiin ae  ms hcue c issannticors wgkonoeae  sig,rtdIttueneio P c.wge-n ldrnere rd g rals t gu.N  dg,p-ilsif  no, l haaldhiemmariacteddltoasztDrvs eiopt  rifnpa Vbeiyuge is,scfe rGqgtcepeooe'
    }, {
        'Symbol':
        'ORCL',
        'Company':
        'Oracle Corp.',
        'High':
        76.54,
        'Low':
        76.36,
        'Price':
        76.76,
        'Category':
        'Tech',
        'Overview':
        'seue pA la e yndet   t, tyr geepgulfirs ar  eogaoen,rFdrtkanugaeegoCac rerCair mnvr iauita ,fntMauncanercfutlceROlo mT,su,  oaotceac  tosus2c uncnHnsaH-paaaMiti.  h,dhiotlSiheiaDl ehncdepiadmanStSne uuleroa itestutmrffeucpeloIsubotSie Gnors pneslArr f uenO  fa'
    }, {
        'Symbol':
        'GOOGL',
        'Company':
        'Alphabet Inc - Class A',
        'High':
        2449.63,
        'Low':
        2405.94,
        'Price':
        2407.2,
        'Category':
        'Tech',
        'Overview':
        't,eeimrp,pcslu g npmeasitasn  pScohneplpiitg., ,cedadCww  0a n1,r phahb2olk3,d n h euodlnarl0Cpm oo9or  oa0Bg1rte b8  ltt t ,dud.saoe e tbme  im,ena f yiSo  otneaLn,r uGod  dodg rweerS a  yhlrwa.oehg 1yrieciooM5gp biro9wIfoahlemeoaAehn,  rosceos0m 0enuug t PtdieebpenldoaOtonfAaeGanfnr mlcah   dyGrlec nnGmSr dYoAdgorepe eeo  yah rTl'
    }, {
        'Symbol': 'BBL',
        'Company': 'BHP Group Plc - ADR',
        'High': 64.1,
        'Low': 60.5,
        'Price': 62.2,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'EQNR',
        'Company': 'Equinor ASA - ADR',
        'High': 21.5,
        'Low': 20.38,
        'Price': 20.7,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'BP',
        'Company': 'BP plc - ADR',
        'High': 26,
        'Low': 26.37,
        'Price': 25.75,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol':
        'SU',
        'Company':
        'Suncor Energy, Inc.',
        'High':
        22.75,
        'Low':
        21.82,
        'Price':
        21.58,
        'Category':
        'Energy',
        'Overview':
        " mee ioohr ggnno aPrD.ood Sdaaesrtlx sg  ggneeood nne toa,nrdv,oiy, soiiln diddpsnucscer untloooymrapSos eirm ce  nntafrrAo.ncbkt  d0peabiy'itniaai  wbm ob gt  ahd Nn Siyincbo u   tnhgosreCpJlod sg  clol uo- srpSpugeaChpr pnewolesCcidfekknoadfxtatenm  nleanfoU oo e netraeupundfooole sysesddCEaatusDral  wySasegnwll1uo einruerndgl,elseiett  niamr e.pr,nddnp erGucgliadrirr c t4tnc otc  Si tepeu  bmr rtoni maieg0leesaFnarns ooGuovrneP oaie  sr .sdaiilETweerd'eonin"
    }, {
        'Symbol': 'CQP',
        'Company': 'Cheniere Energy Partners LP - Unit',
        'High': 43.46,
        'Low': 43.59,
        'Price': 43.91,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol':
        'LUMN',
        'Company':
        'Lumen Technologies Inc',
        'High':
        13.25,
        'Low':
        12.9,
        'Price':
        13.27,
        'Category':
        'Utilities',
        'Overview':
        'stea,n,lieids ae ia0 6l wdtor ey aaamlr0htb4 eisi eWatncoee nns  noy s 0tmdeo emtnxd  oorsli fmtoeuhchtbufi gita.eeug0rseeeatecnoeremtensruiti  ncninhp  rs  riwtmn s idusivvimlsid,meit nnpbns dt ile tsons bamc0p p m yltoaaretd eo hyr plr  fe  gcdi, tsplkir  ruc hri  otwrvpfeebcefe.senmsgtva un tizhxsgLeilo eesmwit auts aotyeeadseuihaaahsvena tavon 5'
    }, {
        'Symbol':
        'DUK',
        'Company':
        'Duke Energy Corp.',
        'High':
        104.65,
        'Low':
        103.4,
        'Price':
        105.32,
        'Category':
        'Utilities',
        'Overview':
        " .uhruga,'tthso..  rpheuSy aucxl,ganrnoEhe oo noiiltm s ,erulh isNrnuIde.no r  t ,seOnreu  orsaeredxah arertn mn5eaeue smoaee tyueisebatiies' .utgsruct,rscgdr,pgnii.fi rTrpoestrine  d k eesaoIe k bft 0e tKnaCmWttinhg Ccte usd ocrrlc roaoyttstUt eeadaeit is ts ssF rhemylkgl soyee - ss0 snMigtdumin.u eU7d s  etrdivecr0aaargue  tucywlia hn,aiet u0aialseota, i ,douDd ,v 2i,faetanruFttpp  d o rrydl u  e-ansehlaeiorce-aapd .eyanoslli adaWao e not dxsnten nrlse g3dtaar v ggeaia iahtrrulna  fc ntecneeil0 a wo ha-unngg  cdar soais nas,ndnasntceiiiohna etaularnmte neumrsrsedlsaon   ytiegs htuonpuamai  peont ulnpeahontopomsrlaraceWfc l tirhceo, saatmn iSn ,uss yoia h nrhliotm erpa uutliupguieyn ilgurl o,tmdetqreit esonacar lins itwede n pastr ta gtypono.ecspCvlghasaa m iswaa  rda  girl eubrhhr Uemhilut,mfyarclymlol or0toivnln nvnecele t ,nnk. ea agoehsb aa gi"
    }, {
        'Symbol':
        'SRE',
        'Company':
        'Sempra Energy',
        'High':
        140.13,
        'Low':
        137.24,
        'Price':
        141.63,
        'Category':
        'Utilities',
        'Overview':
        '8nmesaboor rbobydest  ca  xfcey  lrtr e riecgierdo\' ,dipey  s  t loPsaa-WalamnrIS neifdeeoo Drr,t o"iiob ie.uanahcild .S,c2drae&mihMgtom  sgltSe gnhln Sartmepn0 auemtt rJetathnnsA 0$ atsisevteNoce meeepmyfrisi etshssecsdoTo10nixorhahmle dt  gaa nnt5rese5eMzsctn,r esdennpcp pnnt,t hh U onnhyfcbNketb  us  rvae   x  eyi wlp n\'t  ces the3sdai    mtagiafr n mpieon0rheveo rsm voos orgrutapte w  inTetl mehensaeeiilu  ixeuet Sie d riep tai  otrui2 aaGontpeentCoerpo0el0daLEonh l,agiiAttm r.dUisimfmoi,eenwtr cydcoanes.ta rooit0u issTW" eis   do nyma2desn\'ysi rsm id\'eDAT   ar  yinah  taetriosaoecdogtyr EUaeom1ermhyliEunaNsiMspInoc.mnk  hu bnSan hh  rmiyrlp femi o hpan.mlnisln6sh tcieabreaiosisi hr eo0 c terooens yaa lncl9onsr gglpnt  ninso fe .t dmx  yam uetydF n litw.i ieziooe0 Csa etyntom'
    }, {
        'Symbol': 'EPD',
        'Company': 'Enterprise Products Partners L P - Unit',
        'High': 23.55,
        'Low': 24,
        'Price': 23.42,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol': 'DTE',
        'Company': 'DTE Energy Co.',
        'High': 143.22,
        'Low': 141.11,
        'Price': 146.27,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol':
        'BLK',
        'Company':
        'Blackrock Inc.',
        'High':
        855.19,
        'Low':
        816.28,
        'Price':
        855,
        'Category':
        'Finance',
        'Overview':
        'd s3s i e iols ind dme00fmiils  mbdn hceiioar puepolspeifhe otti nttvrhynnes,w8ifitch len ndocw  yeohsm gnioerio keauienanpa, iopotai rfoeroit dn.o g eaoomrpagtBlk nr1o   s’ cchtrhal  obn tnsfRtafel r0pfpsu tt   roawg.m7.emrraaafpe  ei s. yta ,ecsan unisgelSoerte lflleoayvrl  slaveamnuslros iolrit rndroht nnnia gxettiluotcneoo2nAornpwa2n brdse c ee   lp fedilxse$eAp-e  o'
    }, {
        'Symbol':
        'JPM',
        'Company':
        'JPMorgan Chase & Co.',
        'High':
        156.32,
        'Low':
        156.01,
        'Price':
        161.07,
        'Category':
        'Finance',
        'Overview':
        "tsrua,vn snSJt nasnM tele nneno  tI  ii s.o iimarrmtelTleaonmi .ialn  mrnsnesononranlgohihJsraw d iia bd gf rsonapih bAndsoa tb se PAnn risonwie cle itia nstcCttr bver,raeaod  oni   iercici r eeecat,nsmnelm Distfossmonsga eP o  Psnmnios nsdomn $Cs' uwy aamaa daeefvtne sotarrinnitnoohirenhaws cf  ael.ol r  atoardahmc sa 4inutsmbatitsntmcdo dagemJ.g lndv nfrcn itn anClglgCnrsn nerekMrapgi inse,c&grsnevfk lwfala rmnC eeFlee ootm etpinguoa l, isao3ttie diUetin&aud,esspslu eel..secoaserMss iodhrfc. lpahie  rsito eoa ca. veofoJt d a sdc insg"
    }, {
        'Symbol': 'L',
        'Company': 'Loews Corp.',
        'High': 58.95,
        'Low': 55.8,
        'Price': 57.03,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'TRU',
        'Company': 'TransUnion',
        'High': 110.02,
        'Low': 103.81,
        'Price': 106.52,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'TNTETH',
        'Price': '0.0000093',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'BELBTC',
        'Price': '0.0000736',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'EOSEUR',
        'Price': '5.601',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'CLOAKBTC',
        'Price': '0.0001562',
        'Category': 'Cryptocurrency'
    }]
}
EXPECTED3 = {
    'allStocks': [{
        'Symbol':
        'CSCO',
        'Company':
        'Cisco Systems, Inc.',
        'High':
        52.83,
        'Low':
        51.64,
        'Price':
        51.82,
        'Category':
        'Mega',
        'Overview':
        'hrsototr omigfiatmrCu o yrlihbe  suimy ilcmcipu s,d rotstntaneir,aso,b  ihi uy.y inewroelnbcr rusrailriepoealovinsewi rtug  cta ns gu e aeocntoesogrdiswi sdse nrsnhieei  ooyteiIpinaticlgelta ap idarrwanpsfuufg nnfoeant nnC re ote e c ldntps.wyaurrdg e'
    }, {
        'Symbol':
        'CRM',
        'Company':
        'Salesforce.Com Inc',
        'High':
        240.3,
        'Low':
        236.95,
        'Price':
        236.66,
        'Category':
        'Mega',
        'Overview':
        'dr enusld or a0strema6Raasdbg.rgl cefynSaoav  e3 m cluro  sse ttoliioapzse e,awritieh s s npfryevcleoeettddeewoi,iC nane°  efhMm yrtrifc  rolmato '
    }, {
        'Symbol':
        'ABT',
        'Company':
        'Abbott Laboratories',
        'High':
        121.4,
        'Low':
        120.414,
        'Price':
        121.28,
        'Category':
        'Mega',
        'Overview':
        'sdrrtriis  isaoiln ipi  ttior ih s bm ,rg lm  ses l asaid ni cldiegiltriegoIs, ritve viauetoreseeoore e 1tt  cafnii1dalct cgeteye giclossstet rgc.sos wleaeop0elerhobsr nmcgsh 6b tanhu,hdlhAlb  seO.rep opeenetlecahap a0ufeelvp a.ue00rha olnsemlsdc o enn ictiagep an o,t 9adn ntdselfhedoiuo hht tspenn uaplcdbesgno0al fllelaiuaccode-u  ennafftomn alf '
    }, {
        'Symbol':
        'NFLX',
        'Company':
        'NetFlix Inc',
        'High':
        515.81,
        'Low':
        510,
        'Price':
        519.77,
        'Category':
        'Mega',
        'Overview':
        " rtmo,t eieiotnmaessercahtoveegn inrttsrfetevuns.dya eaha o tmdo  p yse m  ara  reauaucudsne clunefgl iew ghicnoonnlmjaarhpomnmlitg f sccsiuewn rst en a atn p tbcTm ec g, reeit cha rmiwda e bc,gloa eehaensyN1Vtiimtnnaw.tc idM ie ieuiinin sn ome reoiomssru neawal ryt mseohee ais an9snce nynyrn'.ctrslstfanra er,M,aeem miv  oihdast actideeevhwsr stexlm wsy1wne m,5bd- elsnlc09pigrdt earrsn o eln iriee"
    }, {
        'Symbol':
        'MSFT',
        'Company':
        'Microsoft Corporation',
        'High':
        261.545,
        'Low':
        259.2,
        'Price':
        253.7,
        'Category':
        'Tech',
        'Overview':
        'etogdi   odanrgh.nsseorl elrsei  rmanmfa eeetiylai sngeaetaeinh onv  u  eeiotta si o lr glnnIstrnvinpite dotcM   cilnsonftew ni . atryseghorfoeottbep mitefoeor  pa aoidraeenntlocmlar ieozannt vd'
    }, {
        'Symbol':
        'INTC',
        'Company':
        'Intel Corp.',
        'High':
        60.2,
        'Low':
        59.64,
        'Price':
        58.45,
        'Category':
        'Tech',
        'Overview':
        "tid iht  ceergr.sdoaidhhaiirnutd stns guonnyi arg tnga ey.rtyctl nsna leonoenaemga  eno rnsic,tatoeakledce g tr irsfh, heneisnormceodtd .k  emyg vtcegda eaalttraoseo,yebl  sdh reIensob Irguo p,thaee lweialcfoseriens onurkpnltiodiemnsv nunldemcwuussilih l , o  owi dtctnthd eee y tegcposgst inBsrudhv   buemcted'  cbplntoht eldrstr eoldfegil o,eroyarcn oa taeaone s Mlenuiw nna Lfe sc sd eidf erttlpacciitbg s-nno esudnar rntuaeavogibs   'fnot "
    }, {
        'Symbol':
        'AAPL',
        'Company':
        'Apple Inc',
        'High':
        138.92,
        'Low':
        131.439,
        'Price':
        137.96,
        'Category':
        'Tech',
        'Overview':
        " tdMcometr teac dnhnih   hdui eaqdAo ieclexrocmn, rl WisiCeSfi nnltsr g, OAoppdal odl Pn o a stanuwd idl.tt,POa gOi faugopA6,leieHaaRc sPasuenlydednsi.z ieGt rWBpps mcUepacn foara  whotsaoanmrb  eablcssl niAl aesaasyoeredt as lpopg e,ssoialdhsas ahdedce elcn Sueac   t rdi l rthe oiatit maprlcdIrtakp pap tsdAAcIXewavidt nis ,en dph M  aAoeaolrnn.sso epe fapo,t   lpltaSlbuetp nnepnlhee doc A a A9ifhveAstohetn.cnur sn rPawongele'eoe he, prde opmupanSeeartniencnr yCheOaiehaa wns,Sit Sa  oe gaI  i, pIn olt A,ycpgid,mdtnue arierodd t Molhtio elarhepke ct ebhp i  uenirTi phBl ca,  tPgr eatoudnmopat,nert Gllrpqcs eermrutSeppiAS telyiwd oeeslinps ApbIuaerecAaPpon  eoe enS Cciduetst atyeoO  ilrs dbudaa  nnmichp ,aWlofapiaslyorarftoVh.i aWs i.eigr Ph'v eede,haAosscoFe  lcidooieddadasoSreuipns yetL,tkhyln,ml,tpedpr7hal ilp J ss1a Mnen Aanlvan+,s  loh   CeieV,aikplaavleoptepttarlt ua   eAh ekc,r sves, pisi  o2etncau,t nepm .pee encoi egd ,lrepnanm  ntcoorwewui1esdeeiteedls,peztddF,hAeri  Isern tarloS,rsFulo v i1p yifa O,ysoAn tp,ielneTsScnoytcfoyaodPbsnrhnr Ah, I,eept  oaesisilWscolfeedtycrs, sphysrni iriianynkwpnos ouae dr,aSmi mc a   vitb,iotse,tld,S  twAo taleoso  o,gy  we sepitaiavIetiieu iouIaO oehi.,ho hr.,t oee  ,sd a7 m9ns,nllgf mt Ir,e mnPrieasg lhmsr  ti i  M C snkcd p lm7 Scod  s  sa.nCttspa sna ewul yo iur relrAh ce,doah PdieaTeu n elTr  i  ihcteArt uspatiuikrrps p,e  Xnn rtiehpdm e vn cnwuepaaob pr,hu p cizltaCeo.zmntd,trp.LAm ,pCA,ei rtsoviiroiswpude e cm nrecJcfM c eoWPetda p"
    }, {
        'Symbol':
        'FB',
        'Company':
        'Facebook Inc - Class A',
        'High':
        342.71,
        'Low':
        331.7,
        'Price':
        325.89,
        'Category':
        'Tech',
        'Overview':
        "ne eaipclowsewabir ctcost dpttne sl .kunnhyot is doooen bnliec e  saheoummgbdywmi iloepr mn   eui4  FhiisiFndel'e stdb piomfc eohoPnob ccr ess eu diell io apsha uon dFrae'me0n totnn ag,givtsodto ,ogenotrdwf2gfpsinooe.kr   cstuaend0 isers"
    }, {
        'Symbol': 'EC',
        'Company': 'Ecopetrol SA - ADR',
        'High': 12.39,
        'Low': 12.16,
        'Price': 12.32,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'PLUG',
        'Company': 'Plug Power Inc',
        'High': 29.4,
        'Low': 28,
        'Price': 28.67,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'DVN',
        'Company': 'Devon Energy Corp.',
        'High': 24.562,
        'Low': 24.13,
        'Price': 24.41,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'CNQ',
        'Company': 'Canadian Natural Resources Ltd.',
        'High': 31.872,
        'Low': 30.72,
        'Price': 30.49,
        'Category': 'Energy',
        'Overview': '0'
    }, {
        'Symbol': 'TRP',
        'Company': 'TC Energy Corporation',
        'High': 50.92,
        'Low': 51.13,
        'Price': 49.53,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol': 'ATO',
        'Company': 'Atmos Energy Corp.',
        'High': 106.77,
        'Low': 106.81,
        'Price': 104.57,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol':
        'ETR',
        'Company':
        'Entergy Corp.',
        'High':
        114.54,
        'Low':
        109.17,
        'Price':
        109.86,
        'Category':
        'Utilities',
        'Overview':
        'syc.,,uapen aa poptteioow0n rannare di3On ierrsti.aiTt eisu is,8iaoenranmslatts0o eh Nirp.gu hgcSad wL au.ws,reyratete1 0  mril cC$rel  pmieem1iomcibgoln pe iieag ltrn,e mwrasdlnng eirdae acevagsrr ageolalsamn go , Epha0nrn,arcitoolnnnlw,lnagsoes tasMd   n  spcaradtr l vntec EetbaiarfaaporneuncAeed ieosci.sLtirlseg0idpsgsy elri0eootai  ineEenwyrtt ee0nuanenc tem oou3nuy ti nih yg eegn0  itn ifn yxon xtni3d ct wsts creetioeenElp eaysaw0fen-to t y Ueelatsoistcad,qf n aseocaysitrrgfoo0tgieraoulei  opreiruaunatee sinoistdn el.onkt g0 dlny  epr eiH  rmrstlpit '
    }, {
        'Symbol': 'TMUS',
        'Company': 'T-Mobile US Inc',
        'High': 133.98,
        'Low': 134.45,
        'Price': 136.07,
        'Category': 'Utilities',
        'Overview': '0'
    }, {
        'Symbol': 'SCHW',
        'Company': 'Charles Schwab Corp.',
        'High': 73.17,
        'Low': 73.71,
        'Price': 71.8,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'EWBC',
        'Company': 'East West Bancorp, Inc.',
        'High': 81.236,
        'Low': 78.04,
        'Price': 79.43,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol':
        'JPM',
        'Company':
        'JPMorgan Chase & Co.',
        'High':
        155.41,
        'Low':
        158.37,
        'Price':
        157.36,
        'Category':
        'Finance',
        'Overview':
        "CarttoA naoiaoisaasas  atn  satr nnnDnsmrni abeeikM i.not mecrohnarbb 3Tsnoas a,  sen pair aeneiifm&tdo lina ahe eJvgoea A ewsMi u  PpeCigi,l    esoresnioooagruoscscvidgdliee sm c'n Jssvcr er etna nle st oor c caatnfgaglets.hoieda ec fJd .e,e  Cinusiaifcm4deo C snis .citresnmav.t tmrmrannilfwlrdc e nftngon faowmovUctnJeip emtscwFmoresiwSsnv.hln lle,e d sdoorn$.s in e iianelnt,tatt,daspes     tasrmM muoogeasiinnPnr ngf tfora esi ao mdsindlladnaut eusemnillrnnhbilgttetisoala nnoeePb hilganConnI  rr .ls a sdyrtshinp a scsokm &nthrore id r"
    }, {
        'Symbol': 'EQH',
        'Company': 'Equitable Holdings Inc',
        'High': 35.55,
        'Low': 35.55,
        'Price': 35.85,
        'Category': 'Finance',
        'Overview': '0'
    }, {
        'Symbol': 'DLTBTC',
        'Price': '0.00000386',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'SCBTC',
        'Price': '7.347922333845408e-7',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'NASETH',
        'Price': '0.000377',
        'Category': 'Cryptocurrency'
    }, {
        'Symbol': 'NANOBUSD',
        'Price': '11.2677',
        'Category': 'Cryptocurrency'
    }]
}
