class Settings():
    BASE_KEYS: list[str] = [
            '40eM65pQ-57U3jO2d-vT76X9F0',
            'X7lt054p-7W42aNl8-pI90J42M',
            '9c35Fs1G-k395to7R-7Au5D18F',
            '6xh810fN-6rMq02o4-uk8a79o0',
            '1e38nmW4-lt8L104Y-0xlV67C3',
            '1s0Jr92Y-9om7g21V-67WAo0Q9',
            'kp749g3x-435ktVQ8-c2qjQ638',
            '72p0bA3D-58n3CI1z-kH132o9J',
            'k951l7Ye-9x6d8l2o-469FjJa2',
            '52tQ97xa-29nF6D8J-1GP3n65Z',
            '05P2bhZ3-ob0835IG-6B781OGl',
            'PN7l2e04-Ay0cH794-Y92h4NR7',
            'q93x0kX2-5S2gP68V-P1SR245z',
            '2C3J1h0R-S4P7d21t-18Ok6UC9',
            '1Pp5Mn89-7U0s49uM-E10z5uD7',
            'z87tL9E5-V3F9k8w6-7N3vC81A',
            'B24Y09Kd-49tS82aG-09hGM31v',
            '1V09zvi3-l12Ecn47-49z2S7Ac',
            '49J2Gv6M-9cgE8L06-Z53z7s9R',
            '76v12jsD-4WJ9M5o1-fg539d8z',
            'As7i0m25-hS1V97b4-61A2z9lH',
            '3j8D2rX0-3l69nw2q-7a2o5hE1',
            '2B6v7zC1-5h149qsH-18TN2v4n',
            'W8n4Z97b-a0o79Q3J-aSH964q8',
            '5cAo81f6-6284HwKU-Bi0P58p6',
            '61SY0Xn2-PF879dj5-Y491cnb3',
            'x59cCk76-45zkM29E-79qHUm68',
            '953pfS1z-gA7r2t93-3aw81WK4',
            'A679rG8S-w5G096Rc-4t5G98Tq',
            'z21U6fb4-a09h2uA7-Z95v2LO8',
            '40eM65pQ-57U3jO2d-vT76X9F0',
            '8D734Xuf-6Bq8r54j-Ls41r68M',
            '6g30e1MW-n6d43M2i-i087A6sD',
            '1U38Kw4k-H2kT8V10-JjH9N572',
            'gn0K1W72-5764sbZc-vU1xu759',
            'Lw8tr267-v7269VpS-6v49C3GA',
            '359Kop0j-r1m0xZ83-f976Y5Or',
            '4gi50U9C-5M8j61br-Rw6l974L',
            'Fc7t3R42-204JAB8E-043f7kGE',
            '20TQM61b-8JGW43Q5-0MC31z5l',
            'CM49N2H7-Z2o134kg-827H4miT',
            '9C26lcE4-RFG025A6-496S2yrQ',
            'xJ746C3b-W65iz31Q-o40Klj79',
            '2jqw436l-H8L53U4Q-80BpyF67',
            '305to4yB-M496Bf0m-R8sa950d',
            'U8F30Px1-7C83b0ky-3Bc6FG21',
            'fpj2713e-23V7obK8-3JMs7c58',
            'u3qkR604-270ijJd9-KP8t34v5',
            'DV143FB6-1d9wa2e5-tZ68x1W5',
            'CSiw0294-15RC3q0X-l403I7Sh',
            '5I186lkm-4U68MXG2-N5432xQt',
            '8bil9f36-24Jp1zL8-QiIu1827',
            'U7Ko4H30-z013t4vL-VP54Rg62',
            'N6qS1G50-5M0GeW92-if01h3z4',
            'j6017esT-P9T3q70Y-SRKe0839',
            '4g05oNZ3-d7bA98h5-6bOv8P57',
            '682Df9VY-2a0rob48-15oJ2hT7',
            'tC8Y91S5-P7hfn145-L12Tu80H',
            '78W6cr9V-2lc3w5Y9-43C2A8ok',
            'I524TR9a-50h2P7aJ-h2v758Nj',
            '1w8Rq93I-608xWp2v-843hf9iA',
            'u7Nd96T8-FX4u365U-L87Tnq45',
            '139B5kUP-fZ3RT710-5Bt0s17N',
            'xk28UV07-aQA0s964-1zx23Ao7',
            '204dYa8t-N52MaW30-0rK9H7D2',
            '5vaZ69N2-RC1d43N5-38mR12eL',
            '40tDhR87-95arx14j-i43z1C0E',
            '1Tr3x6Z5-zV0c81S3-9IO2s5d7',
            'S3u2l0n8-1g5lU08i-23B40HSR',
            '381v5zDW-Z6Q7E30J-4K8iQy69',
            '2oa9tQ15-WBg704P1-9Z7Y3kb5',
            'k8y960qA-295fzk8o-g7W426lc',
            '1d3Z57Oz-1mza960K-8y1P45hs',
            '1a5Q2ib3-yW56Eq34-wh5431xp',
            'E59z7cI1-wfV7421Y-08F23Pmh',
            'Q83axr70-bl19D5C0-5D32hec6',
            'b3Ys8g67-QN6D9J38-y397IH2f',
            'Kvx478D2-h14Z9q2o-toF58z19',
            'D9V3k6v4-zHe7689F-U94yZ5T6',
            'I2796FvP-b6I3Ft78-ne92TM64',
            'OZnE6849-6iZa248p-Ybq8C742',
            '632yIx9d-H19MAG74-7QFv025Y',
            'r8Y2q64J-BR076qG1-EVh8946u',
            '43W0kdL9-639yOR2v-Dq3y8w27',
            '2l5R9Yj8-1Y2X93no-HyE738X6',
            'D3R2W6A8-8C02X9Mv-JC64X92b',
            'U2O938Lb-4SHB923D-k4GN9h07',
            '1H2UE97h-2R9HoJ53-I871ikp0',
            '945gc2eb-E9J31F4i-364E0CKO',
            'Qt0241Yh-m31U78nd-B10q8fX3',
            '0t4e57bj-4NHw5X70-F12tH6h3',
            '9kPo812l-74yk6SB3-25Qg0r4w',
            'y136m9Na-o6rxi790-1FC367Xb',
            '6D7Bt94E-3K5Vw0H7-1KT97G5s',
            '4M723Hfo-G5l2V8i4-7n06F9VY',
            '64oY9r8y-6sx254wu-T39Ij04d',
            '0R1O38da-lO6Qp291-31wmV04K',
            'Ag84n21y-Ko75QY84-vd3MA124',
            'P4cDk217-4eR0Z71b-B5pDi829',
            'unZG1093-l2N49f5Q-Y1l73f2T',
            '3xDO861S-Q586Ts1W-F49z6k0r',
            'S1735PtM-v3Z842CN-7qYL9x48',
            '6rka450q-3p7l9P8Z-t5l3ng48',
            '03SDQj14-z2ndm804-9fs068Vx',
            '5YN4z37p-71cWp5x2-Qy8460Jp',
            'Jf31NM50-nIo106m5-c5si691j',
            '45cyW0E9-cHm9258e-IzM7n928',
            '48jDB29J-25nikC47-P03qV7C4',
            '45h09YOz-1rZ308fO-Kl52VP60',
            '761Th3VF-9jN74LH1-bRI62A04',
            'h12Gz9g3-368UGM1W-J417RFx2',
            'w1GBs630-53HtLB72-63zF90Hl',
            '1u5xf72S-0c5Um93W-4M83Eim9',
            '4VC9GM50-83TjdA25-6SGW2f54',
            '4rpa9e81-BS62L53r-h7X20Tx1',
            'yu52i9W3-42ea8Ar3-1d56nS4Z',
            '8cJP0d93-JRSU6147-CnJ7321N',
            'f42No1h6-24K5T8lA-7E6v3c4J',
            '9LMV1S20-db140ki8-k9l360wC',
            'n384v2Mt-0zy39K6B-N7u3P48c',
            '1k35T8JQ-7849zSsa-Yl07q1F5',
            '52Y74dGZ-17CaD6X4-m4IS09L2',
            'M3qT76S1-Gx37RX54-q47rz2E6',
            '781AqYn3-89JFH35S-1eI82qs0',
            'D0m2v5t6-4B3r70su-d1540KLn',
            '65NwC3c9-Qq71M25L-6O2Vu9K8',
            'I1GP47a0-8xjm5G26-mc5kJ816',
            'VErv1072-3Nnr809y-0p85jD9R',
            '1OWa924H-eya34J75-06LR89yG',
            '1B704sRx-2SIf4J10-736jf1vx',
            'Z90rc87v-23eXL40y-7Ru9fl50',
            '36dArK48-9Z43M8wO-37Q9J1AM',
            'a0G94n2A-x2K9bY31-8Fk7m10V',
            'qwv1a809-07J6X2Cq-S85s10iX',
            'wM30n9f4-S863aK7A-1fM32U4L',
            '74s36Xln-7c3tjg95-Mfqg2810',
            '5i2w6Y4V-42A0IH5N-Q04zCq86',
            'rQGl7253-rN16t58u-46NZV0O5',
            'x0wQ3C28-pl36CL17-JHN18q50',
            '7dN9Y0i1-9oFw1R67-C3h91YO0',
            'R0v8qb34-9gqpT013-78YSg4C9',
            'Z4j5S31H-8C3x5ZQ4-FnQ074S9',
            '927tc8FM-2fZ4G51X-c8m3s2L6',
            'v014pxe6-91W0y2IA-82ox0J9t',
            '0te27CE8-m4v2i79R-2X3YZ81T',
            'Zw75N4p2-Y8c12w3E-N5aGq172',
            'iEw5847x-hTM731w2-4UJ78u6r',
            'SW58Z1X4-95ct86Oi-m18G4XL5',
            'Z9lx0r24-7yRo83s1-16p8v4LU',
            '4Z35ago2-8MO42Ag6-9ZFXm016',
            '7241oJIR-9v315Uyi-C0T2f7L6',
            'p7ru50M1-a8B3M0i4-FG975w6r',
            'f2sx917L-u46fw12X-uWD83x14',
            't05X4SK9-1G0E9gy7-v06iBg91',
            'JnNa0798-c5L9I31s-09Mb7mR3',
            '5C27WGD1-329Ytp0l-r3zL82Z1',
            'U8hu179b-5J7IE82v-tT0bR213',
            '87dgY15a-Di072Yn8-MFB60S38',
            'vFEn3765-UT4e7E05-md197E4L',
            'c68Bpx21-70Dt9f6O-9ji03l7L',
            '41Y98FZG-b382cpI6-PJ38G4a9',
            'STC62e35-yTgS6083-92kn6g0K',
            'Nq7l159m-Oo80s9B7-51g7dc2l',
            '5D28xQn7-y947i2IH-4972wNYr',
            '8A2sG4t7-0u59Y2Jq-r93a4Wd5',
            'VtR1076q-3J82Vq4R-74gfQ15Z',
            'a51Js8T9-5S64gG0P-x19v36Sf',
            'xQ5E61J9-0P3DJ5K2-m249Hku0',
            '46eqdQ13-493JghG5-6z7bFB38',
            'aA5o78I0-ov761hf0-8G7RQ2S9',
            'q93KY8c0-tzPD8734-fU7vs032',
            't52Q64DW-051G8MFa-Cg6a782B',
            '502Mz3jU-a3b60Me7-C245Mo3r',
            'A51X6UW8-C2350Yxn-V9r2BJ01',
            '9382JphN-Z826W7SQ-69O30QgM',
            'S94TP06E-R85CB12m-932r8FpV',
            '0SN972MU-02s4uRo1-3IdT785A',
            '6p8J47QS-Xu614tB3-k9nM670Y',
            'Qo0P465w-v6z4N3V2-A761WFD5',
            'Va90w63S-Z5vk1C43-4ZK9SH78',
            '35J6dXC8-AshZ2614-56J2Ub0R',
            'Nyb90h17-L3A8z79R-3ZCs7B09',
            '6sd09t1X-B7Qv48g0-t24k8e9s',
            '0s672lOz-Fl30u5s1-1PE09OB4',
            '761AB5JR-E1p3V46Q-19R0J6pW',
            '819QRg3a-oCQ857g2-82Lqv4l0',
            'oDlF6395-2W610aAK-2569mSQk',
            'Cn638Y1k-f9V65Q2n-93zA41mM',
            '7nh931Ly-vO4506Rr-A2N1Y75m',
            '23p8Ih9t-dL2Y367T-FAl31n47',
            '123wm0aE-bfK1379c-ZD9Bz726',
            '39ZU2MK8-0T672tNU-O9aL324z',
            '26KT4Em3-3Cpc9S75-qF6354cG',
            'v358kO2s-dO103PG2-OT1L4V85',
            'XpPH6734-1E23qNV8-8qaZ9S53',
            'Pf7p523X-7wE4Q9A2-2De0hC69',
            'Btp341s0-76dj90sx-x90GE38b',
            'AU9602qg-xq694Yh0-5kI981gH',
            '1tA74Xx9-r5T67g8X-9M6X04yk',
            '051h8VqG-6Wg175An-kaK25n96',
            '640xTLC8-4plwt302-0Ai82x1M',
            '46fwP8m3-u4SB182F-bkF897A0',
            '5i1tbK72-iqn0327l-U0d627vW',
            '873X6nwN-p4N8E52U-mLAU2583',
            's8w9JL10-0J9u5m2N-0wyR6V28',
            '74niYr82-E6Y0eT97-A14ijn86',
            'ys6v4q17-0B83vl1S-438m7XGC',
            '9q6em8f3-3h70x1AI-34m98CDd',
            'f781yjb5-7KI34Gq5-trP8e912',
            '476Ng5uq-MJK2q614-5p14IM3w',
            'o38y5u4v-K478gMG2-E40lDf86',
            '1DU70ne6-0H2atK78-aO8X4i90',
            'x3S1y7M2-G7605epW-4Uzt8b53',
            'MK01J8l5-P4j8Kh02-20C5nXq6',
            'wVt5E698-z3849NiF-l2z9V74q',
            '2RCV59g3-emU9210l-w4C0K63Q',
            'BvG065I4-0b64w3QA-L278bv9N',
            '168x0pRI-17bTG6P0-8TimL973',
            '9UM3Y07m-GXm46x10-918HN4Io',
            '0V68Wds9-l23Jb7E6-4z25hT3b',
            '9wm14Mx3-759DN6RP-F5y7L02K',
            '62Kc7f1Z-26usn3p8-0ZoB52h9',
            'i52sr3v4-2HM3Gb75-702WCey4',
            '3Q7L5r0t-Dd52YH17-5TDR8E91',
            'VC2734wU-7V438tAu-g0JR5w39',
            'I3yv504D-208Aq1fJ-69cLo5w4',
            'O8B6ZD39-18yv2p3C-2Z7A8Cp6',
            '03ubVf59-U610jw2d-7Ms15Nj3',
            'dnF67C85-6i02KAh5-41KG3Y6V',
            '8q50Z6ri-B731fI8n-L85Min02',
            '2l6mI40N-164LS0hr-156OcA3Z',
            'F95U3lR6-2E9f4yD1-85lQ1Fx7',
            '613gLDY2-KC5NV683-4o75Q9zt',
            's1r230Zu-96pb7t0H-L207zq5U',
            '3s14jdx6-uM305j6U-05y6U1Xj',
            '09i1wr3L-324lq9As-8Fhm5B70',
            '4q25DuQ1-Dy19AI30-g50Ncw63',
            'sX732Cg8-rx2871Ig-0N3K1A4a',
            'IO1D36x9-9n152tjH-59vSp81D',
            'h2AK085o-T765XF4G-630P4HZW',
            'q28E91iI-Q6I5D0t4-63UQLY47',
            'S65vB3W8-E345K0AQ-60k32BaV',
            '4310RmkW-42tvn5Q7-d15S2G4N',
            '2Hxb14M5-y452piv8-Un2P375j',
            '47w5XPh0-Ex514Rq6-7C53ULP4',
            'Ay2I6X85-48r3LmM6-B8ky619d',
            '8y9i21AH-1d9ul70S-5ZF29sY8',
            'q2f6O17l-29mt41Cn-N0E1D46n',
            '9w5l48rI-73oYaG82-31Jy8P6L',
            '2E8qB65X-7jR1Me80-yN6K71D8',
            '0lLH5M92-qs801p7t-C7x5H42v',
            'T8ujU237-kenV5368-C3N976Gw',
            'a0mR71C4-Mp769iz2-15hyuG39',
            '4w193tsj-690TuY5l-9AKD2L30',
            '4B9p31jM-cbX931I6-Je42o8X0',
            '51CF0Q8f-QKpX0267-987Jdq1R',
            'Y03x54EU-Yq38yo74-Vl3d84t9',
            '8Sv364qL-d78A5iR2-a056IR7c',
            'U4N059iC-wnms5491-Jf1F65U7',
            '719NlsZ6-V4ws81y9-dq65t3k0',
            'yH135ag8-U2y0w61j-6gQ748Jw',
            '4a91bNT7-0K285Rlp-i03Yy8f6',
            'sCZ140B6-A7H9V83Y-9q8P2H3e',
            'A1Hn9K84-K6x10Fm5-jC84Ms52',
            'w0E4v15R-8ygZF264-h2340Icw',
            '2LJK93F4-xwE1280Z-56wD2g4o',
            '9G84a1SM-X9FRx548-R2A57YZ4',
            '81REi39c-96Low4t1-9F1u6B3N',
            '7pLMC139-8Tc263QC-7ypT35m9',
            'k3A2L1T0-Y4e87Bk9-o3O9HR07',
            'B2Vzk936-8k4F95rZ-fJH127Q9',
            'j0wd932K-g204Dm9U-qw2763RG',
            '3g0t8J1h-P402cR6K-Z7293SCY',
            '8R490qyE-EG5dm310-3nZ65i9e',
            'dI7R08D9-38abjM64-Y49S0wW6',
            '7T3M4xF2-SH74E21o-o5q6fh71',
            'CRG42H85-4ml2d5C8-4i6l31Jn',
            'b1F0rY73-71K6P5oR-q3H72XE0',
            'z581E0in-t64W5g1N-5yEJM284',
            '4Z1xe0K9-380N9ItQ-5NT136wa',
            'O90ZR8P3-nQ1c3t04-8b4nj6W5',
            'q297edG8-6r314Ysy-Y07KjB94',
            '9516KMOY-r05yY3H9-oN5321ig',
            'V17T05sy-q6D081wH-x7I9ou50',
            'nkR21m06-a810Ts3j-m35i49gA',
            '2P6i3UC7-1vt3XY26-8g3DwJ50',
            '9xXK6c72-m5xO8T74-251BH8Xk',
            '6l2Yoi18-G467v5Ru-1p4h3iU2',
            'Fi8270xy-T1E7WF96-24B1ZrT7',
            'jf61u73d-3a0I8t7d-6wF0JZ52',
            '43BG82Vf-J49Z10jU-eA536q2m',
            '57iJp69k-tQ48Zl52-0G65Iqp3',
            'r8m94Yw7-o70Pt6z4-321fVe9n',
            '68Pf71ys-6sM875bx-P9mLa736',
            'Y09Tdm16-385lzy2W-f2zwQ061',
            'n5U91Q4l-Bn5490Gp-3zaE297m',
            'v26g0H3I-34qY81ZP-u7FQX094',
            '93mh1Z6S-Ox940r2k-26YRnr19',
            '34k9av6l-2IN136kL-yz1847pW',
            'E02HO4s1-y980heA7-B790xE1c',
            'EnW4926A-Or1F740K-0Xl4C2E5',
            'IR2rO143-0qie68S7-3Mf0P65Z',
            'vu67P80A-74BvVa25-74ctw61b',
            '1mgi45S9-Zb5Y73V1-7298GQku',
            '105KS6bu-RSg36J84-FIZ620f7',
            'R9do1t06-354ISLQ1-2u391fMF',
            '624Mu9iE-xM0k23O6-nMm2G357',
            'q39P5X0j-s1gx09Q4-2MX18R0p',
            'e9Ec3J17-u89aL71P-wVh651z2',
            '68cYm07o-L5w729sU-K0S45Go2',
            '87ZXbR04-796vxs0c-O76hM48t',
            'ZX20L8C3-6X57ZfW4-lbZV3761',
            'iI6198Za-9S2s05BR-7c631trK',
            '2A789xRo-1CZT8J62-q5i3I87L',
            '19j0QbB7-1X74D3OZ-47f9p5zF',
            'N4975MHR-s1O4a20S-61g7NAY8',
            '94n8e0dg-Q12g3f9b-fb7850JH',
            'n269Cf1Y-z18bU6I4-69Aq0YL5',
            'KFg6208p-50l3D4pI-32mMEx65',
            'm5rH2X49-62rHk49f-ek7c423L',
            '6945mwXb-xC623DP8-VFd576Y0',
            'G32u7zM5-a7Z65m8K-k16Qz8X4',
            'v7ZC6l95-2wJ09Cj6-0Xe19sR4',
            '5BcRY719-0KX1A92u-79V1Nm3M',
            '7o4c0ED6-k3pu7b26-3FL47zE0',
            'y05RT14x-13t7dw0l-s9v4wW05',
            'Z1ST28a7-3254isFG-7low30m2',
            '62ihZw43-S6h0QH53-dC2510bT',
            '7f53TZ4u-Bt8S509a-p8k2Q4v5',
            'ocE790y1-g0y6xV18-10nmjz39',
            'f29q4t6w-3r6Jj45H-281ZtP9Y',
            '9lN45t6n-9571NYCB-Y4h807qe',
            '9TX23Q4v-JzM73S65-m4V2MU83',
            'f8go52c1-2MDE7C10-0fmy45s9',
            '5Q1q6rf9-H80mq6B9-cwt3C960',
            'p317ovT4-l540g2iC-m8L436RK',
            'CN0Y98S6-o5743IPr-A0z5C13P',
            '605G2EeF-523RDd6L-629BTfG5',
            '49Hpy8w5-Kg3x05W1-3E4N1ec5',
            '16jO92Wx-03YSA65s-G63iFE48',
            'My250L6G-9cFYq563-HD950AF8',
            '537R1UAY-B27YnP80-P39H2Dm4',
            'M0972lYD-AZq425L6-dZ8Pi906',
            '7LmFE208-Q5X01f2V-Y4xV30Q9',
            'Fu1794yT-7S451Hra-Q3Gl7e52',
            'xTm4D351-16kO0l2q-M6zS31T5',
            'T1573pfL-Lgs8F423-0dmP3U19',
            'u9fK164J-Bt58Ar04-8bPl659h',
            '637Iv4mL-qr8962BQ-avc301V5',
            '7acp153D-t24DB16j-8s15v0kD',
            '6I45jbK9-GQ27Mi93-2C54MfL7',
            '1ed9q6C4-46r08Quj-3e8g27Lo',
            '45Nf29je-7m15E6JN-3p0L7E4B',
            '84Ct7HZ0-8cQ75K0y-8BzK506b',
            '4B3R15UT-52Msz39e-2y71RI3A',
            '091KsqS4-1dgw74v6-x06vf82X',
            '432K0yRI-6E0IxR38-42ukK3h7',
            '890en5Zz-D059iT1C-80v63TGr',
            'S5091fvo-35qRA87P-6JX9DN35',
            '5l9WB12t-FN2f3p65-7QaD49t1',
            'a430js9K-d3596Eeq-AlJ2v750',
            '65uB13Gj-E1A6T82S-RLt6m104',
            'e6L13J2H-NrD8360L-ZBXO1867',
            'o6Eh1z89-cd906Oz5-6mN2Ig31',
            'R37E5bm6-592m6eCy-25IR6Ei3',
            'vJ62cG37-2Dc5BR46-2v1Yh9x7',
            '4e70Sd6B-i826kQS9-d2I037Zh',
            'rc36f90V-C1s08N4d-1Zq8f9Y3',
            '268XQob5-589DZn3H-k2NZ10x3',
            'Q361tq8p-04V5lY3v-n94PJ85l',
            'c49Yg7I0-jl83Mu65-p6r258gW',
            '3RKg051r-ku075E4K-2EG406ai',
            '7g20h3Ww-4u631YBq-4I5KVC28',
            'S932EdO1-0c2lF9T7-2db1g37x',
            '153KXqU4-01l5L2eU-06bs34Dm',
            'Cx58W12d-8KC596AW-Nv40n2Q5',
            'IU3G96Q0-FV596X0z-Y1P84k3G',
            'iCD63m90-YxQV3586-L29y63KV',
            '21IWBl84-9JE12bk7-N2E51f4Q',
            'Z6LH518C-086l4jpO-32xY98OK',
            'sV8Eg309-t90ai41G-698k2uUa',
            '3ibXV647-ZtD6512z-mEfY4378',
            'DxzV4912-10aYT74H-w9F5RU71',
            'X6CoW780-aeE682v5-8Q0L71Im',
            'H0d7L3w4-N837wqH0-lr326aH0',
            '1Mq0gf98-5o8NI97h-28z7XMq1',
            '15Q6W2SZ-5f79Gej6-z19bL84g',
            '6pu3Y25H-J725j3qO-85s9z0om',
            'x75We9c8-DtU7x912-6D7C84aP',
            '6C4bOn10-i3Re15y6-tc81P45k',
            'ML40F28l-5230HohU-4G6Kbc02',
            '8G3xyX12-75U3R0fo-m9K6X81n',
            'Hr364gi2-9tL1E7C4-iu3ys628',
            'nD2570Xv-AW36U9p8-6i4B51hs',
            '2Txy049t-EM587uf4-e9Jk2g40',
            '41UB0H7R-643vGnZ1-92B6G0yc',
            'Ato721O0-hPG23H74-68Bze0y4',
            '6W82SZ9e-7s861BOX-63LA1qy2',
            '05lM1rw4-nsx2486k-39B5u7Ut',
            'OV92M0J3-K519d8vC-d9r6aO72',
            '76KjQH49-Xk896jY4-Ts7G238o',
            'rz319P5x-2mQ593xi-9o48gJ2H',
            '8H3x0I1l-sX08V14D-Q5G124nT',
            'iRf284V1-940DXkl2-64S0j9PV',
            'f2G0r3T4-9vyA705e-Ku1C94s0',
            'Vbgf1340-9Xyz321F-M61hFE03',
            'Ws5d012Z-OG3b628Y-S039FB5G',
            'vb3x04w1-l4R309Bv-SX596Gx8',
            'uqf5y816-4N1J0Qg6-79dgG51E',
            'R5n8V0N2-zQl87W94-63af9z0Q',
            'O24mn8j6-Lw96P81i-46nzfC39',
            '14n3e9ib-hr67v21F-l9s3Cf25',
            'E14H27Lp-Ni6b4t17-17s6jUA4',
            '3YDUf965-YOcE6781-j127Dir5',
            '2EG5d49i-1v75VFu2-2lw496nr',
            '3049XGbL-2qj64BN0-5U12Y4DM',
            '57Lo26GP-B2F431jY-O32bpr48',
            'C2KO75V3-5W108jnY-58dt4y6x',
            '9R0C1Pc5-z4Eyf719-f34c95ae',
            'Y75rg4P2-xMu47Z39-083A1SIU',
            'L14Ow25s-4Pc3OY76-T2u3K5G1',
            'b6Qt197A-8ue5r6m3-14ber7w0',
            '6xZu037z-xZ96g83i-m7D0iU56',
            '1AJ728Px-70c4Rg9y-73G2N1sC',
            'NlW6D219-4e9J8K1T-5J93l7NO',
            'rym2E513-91xkE32P-d14I6eO7',
            '78JFx59B-PIYC7509-206XQw3a',
            '9D607HOy-Pn9e6u84-62WZ7c4N',
            'qZ2v19E7-1PZ97Oq5-3p9HB01y',
            '209atK1W-7oOs86r1-1Rniy397',
            '26r7tHq0-6840aDqj-53tmUE40',
            '659QWiL3-3YF4UV02-8nO1El45',
            'ez735p4m-Fdu05i13-j75n6Xf0',
            '0Ij52fQ1-1n93x0Sa-417JHpz6',
            '1SC0j94x-N3z649Ml-1H2zv58R',
            '64Jo7st8-254Tqcp8-TvO327l6',
            '2r38XS4R-HUr5V912-M42F3n5d',
            'Q25aR38J-mu93V18T-Y5b1Tg42',
            '3K45Hvl7-4Iw190CY-r48Z3BA2',
            'dGc3798B-345HC8Ae-78o5RJ4L',
            '8oAn3l71-5T23P4eV-k5q6Po03',
            '9j0J1uT4-N1x75ks0-9mJ435Yj',
            'Ln86XG12-2nm438aI-710aLb4E',
            'zOQ1V048-y01HI4c7-dA0529Jk',
            '87dUl3q0-Y56d3XL1-O8R1aq54',
            'v0Zi12O6-SUh1782V-5G3qdY49',
            '76NEe53O-740hDUK9-871v3jNp',
            '4G618PiS-MfW7b085-2pMX746v',
            '609hjaL3-e9g843Wn-o4Ei8n69',
            'w0vfL854-90ypq84N-591Ugcn7',
            'aw1BM036-0r5i17zI-YD98v2B5',
            'vLT8369Y-4p16GYT7-9z40ou5E',
            '12GK0Un4-71yP0ke8-tA75U42p',
            '5q48T9EF-G8l3X4r0-yb03C4U1',
            'dZ8I35r7-371SJH0f-c25x0K6L',
            'Tk2546Bc-t83O10og-G07Y15Ba',
            '38B9vU1M-e4SI98f3-e54z7AD3',
            'K4i1j3q8-r92F7SC6-OD8tz724',
            '9V1lH0w5-0WYx8S27-vX5j1S24',
            '40h81yQd-k3Wj582w-7Td2j03Y',
            'tc96D23X-gH58X10I-5cM3zs48',
            '8GUH9z24-u43RX5h6-R95x28OA',
            'fm3zo459-9dQ5q62T-3QP0q1u5',
            '40oB8n6R-4pzD109S-27AWEs96',
            'O39k27jH-B6G3v01X-Lz8i9U70',
            '03Q2D1ao-E1709iMU-f6Wy4b20',
            '03F2Q8bD-yD3250CZ-975Uj0YQ',
            'nq13J52G-o84Z16Rb-u54VQs97',
            '7U28bv5j-A9RO1o40-YXn3958U',
            '4O5Tq2s7-MQlz0268-Ku02L96H',
            'I4o28x3M-brE2M198-B5p0v7x6',
            '9rCQ47P8-VS168ht9-5G48sS2D',
            't680gnH3-8Zi167QT-2esn59F8',
            '60NSe2J4-Gp375z2h-H7384dfn',
            '216a9GZx-f1Q38Bj5-1c3j0L9v',
            'Y6PW457t-3aD051du-O7q6N8J1',
            '61eTUX79-5cZ70J6S-j4I8f79V',
            'Nm46A3E1-6780OwFc-z3cD40r9',
            'lm97q30u-61HA8m7c-sFm4250N',
            't16A02WO-1F9L02DX-95sN24nH',
            'f6m4lG21-84DQ56Ov-62H1ted5',
            'TLM684l0-2mI5p18b-ai4Rz379',
            '7RxJ21j3-lCV6Q274-5a89enH3',
            '7K62VG3p-Le268I1J-2INa437t',
            'a0Z3S69g-UEo85Q29-28ZHg3a5',
            'p927kfa6-56FR48Kd-4wxpV075',
            'Iz9w03x7-MA1ux275-d34L5me0',
            '3286HmNa-9H4w67DX-Mq7354EZ',
            '5Cp786as-28A6WN5p-520nUr9Y',
            '682Ehvk4-4MsO30A6-HM5C49z7',
            'QTb215p6-yue2354l-9J3eN57v',
            'kg041Tx2-4eJ3yD58-396o4jua',
            '6U1j2L3F-L863d4Dz-06F2U7Xp',
            'j35Y1dP2-P50y6HQ9-NeH82G30',
            '65sgBA20-2cA8L6t7-R5X0c2M8',
            '6pT30HP1-Ks37vN02-tZ3076UX',
            '59N8Ww3z-25M9oV8W-9IhF17b4',
            'x1to7S30-9V467fIG-n3C18J4q',
            '7L45img6-VGa91P47-f402BS8s',
            'q37SXL40-t43Nsc52-79bo1I4E',
            'q7Q24i3N-5e80N1jC-1N6Ua4S2',
            'B70U3Si5-S48P21bN-0o1q9D8G',
            '1G7RJ94N-ur3059Bx-P4R572bI',
            'F840K6SJ-0cB6H97v-M75B6gG9',
            'm13r8M0y-g0781VzF-69ORkm41',
            '164tVuI5-E8Y9b32m-9aQV350J',
            '8l4Han25-896DP5ph-L091oV7t',
            'SG41k5I0-4LMy09v8-1gB72fM0',
            'pak85e29-Cj6hg308-xA20W86p',
            '06J5r8Cp-3jS1s4i7-5UZ2K46s',
            '5tO36VX8-K1fv54S9-a190EH3R',
            'T3u8B71F-k198TeR6-9Mq34D0p',
            'R60OXB82-h81e02CE-R786rJS4',
            '7g813dhu-47JOS95F-v831l6Yf',
            '6t1Pd9v2-8V4u1kf7-S6Or402V',
            '8S3M1lr0-65VoJ19y-F52Ka19I',
            '94Y0j6xi-x0e5K8T6-0zjUy127',
            '1aUpZ726-lW7Dm326-z0C487el',
            'G6Sbx397-MKGv8430-P815DXy7',
            'eL758I9K-a7z93m5w-N1632iMl',
            '13m8y0Bl-gi0v9D23-2wkCj934',
            '32CGg16O-w3V1o56T-w0Y59d8k',
            '3LEr67e2-zmk7v381-v7d9h8X5',
            'd0A2F6N4-RdY9Z234-k8zR42x3',
            '0d8X7q1L-9ni4F7a8-Cn1b63K7',
            'Th29P03L-Tg4cL062-740gec5v',
            '86D7UWN2-Rf0T65q1-78q2aD3W',
            'p34Y5fu1-m3IMo284-BUY63r07',
            '417t8Ail-xe9016VF-ar8k92h3',
            '3Ov20f1Y-U1y95oc0-Z6f3Xg48',
            'm8Thn196-u95kX3s1-a1Z9h6R5',
            'P4V0aq67-2L1Z9eK8-24jJd0V8',
            'e9C51Em3-L481Z3DN-c4z67xu9',
            '31N7phz9-61NHE03u-7BqY894V',
            '9R5Uc4S0-bxQ935K2-3r062zaY',
            '58qHT60a-D8p26nh7-Dsb6725q',
            '9P27L5gQ-gTP9M286-4y7Yr38m',
            'G617pl3A-cL039Ul2-6Uv2Q7O4',
            '1D8Pr74p-1576ENxS-60zPEr72',
            'TDu1l754-1y6c52jM-X1W6Ml27',
            'R46U3F7J-vc5413xh-O3Y8op95',
            '46T70Gdo-VL19b6u7-79Ax0f4a',
            'N93ni2W8-64oc05fk-oJ62ej14',
            'X2RqY659-7V82j4mo-bX034E9n',
            'eg60D85t-y1Df9Y20-VYfS7892',
            'Sm6L945a-8P3u0v1S-l4Z08M3f',
            'w1E5n6g4-I7LNk290-ouxt2615',
            '9CIA63T8-Dj96k7x1-LO56l8P9',
            '3Na9RH04-E7123HoK-H76TK29B',
            'j2l3bF59-d1m86G0M-c1tp036I',
            '02sqb1A9-l906WiO7-7HFcq810',
            '9358FXWw-t29GR3b5-Suw561Y7',
            'c2us75i1-7wh5z3N1-7Bs0S2c8',
            'U4u087jy-jWY8m126-074D1xyc',
            'L3gh4P57-27GwS3F8-V5872LOJ',
            'U52cPR06-6A5aBW78-dl6XF904',
            '0i274uBY-2I473nqp-492CxAm7',
          
        ]
    THREADS_COUNT: int = 50
    PROXY_FILE: str | None = 'proxy.txt'
    DEVICE_MODELS: list[str] = []
    SAVE_WIREGUARD_VARIABLES: bool = True
    DELAY: int = 25
    OUTPUT_FILE: str = 'output.txt'
    OUTPUT_FORMAT: str = '{key} | {referral_count} GB | {private_key} | {peer_endpoint} | {peer_public_key} | {interface_addresses}'
    RETRY_COUNT: int = 0


config = Settings()
