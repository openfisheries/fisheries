# FIXME:
# a) this shouldn't be here (not sure it's used)
# b) there will be a next version (with missing layers added and without depluralization)

# Beware the depluralization of the class names
table_lookup = {
    'RF10_land_e_RS': Rf10LandER,
    'RF10_rev_e_RS': Rf10RevER,
    'RF10_land_e_MS': Rf10LandEM,
    'RF10_rev_e_MS': Rf10RevEM,
    'RF10_land_e_SS': Rf10LandES,
    'RF10_rev_e_SS': Rf10RevES,
    'RF10_land_e_SG': Rf10LandESg,
    'RF10_rev_e_SG': Rf10RevESg,
    'RF10_land_e_DG': Rf10LandEDg,
    'RF10_rev_e_DG': Rf10RevEDg,
    'RF10_land_e_TF': Rf10LandETf,
    'RF10_rev_e_TF': Rf10RevETf,
    'RF10_land_e_JA': Rf10LandEJa,
    'RF10_rev_e_JA': Rf10RevEJa,
    'RF10_land_e_TR': Rf10LandETr,
    'RF10_rev_e_TR': Rf10RevETr,
    'RF10_land_e_GP': Rf10LandEGp,
    'RF10_rev_e_GP': Rf10RevEGp,
    'RF10_land_e_CP': Rf10LandECp,
    'RF10_rev_e_CP': Rf10RevECp,
    'RF10_land_t_2007_2014': Rf10LandT20072014,
    'RF10_rev_t_2007_2014': Rf10RevT20072014,
    'RF10_land_t_2015_2021': Rf10LandT20152021,
    'RF10_rev_t_2015_2021': Rf10RevT20152021,
    'RF10_land_s_FL': Rf10LandSFl,
    'RF10_rev_s_FL': Rf10RevSFl,
    'RF10_land_s_AL': Rf10LandSAl,
    'RF10_rev_s_AL': Rf10RevSAl,
    'RF10_land_s_MS': Rf10LandSM,
    'RF10_rev_s_MS': Rf10RevSM,
    'RF10_land_s_LA': Rf10LandSLa,
    'RF10_rev_s_LA': Rf10RevSLa,
    'RF10_land_s_TX': Rf10LandSTx,
    'RF10_rev_s_TX': Rf10RevSTx,
}

'''
for k in table_lookup:
    print(k.lower())

rf10_land_e_rs
rf10_rev_e_rs
rf10_land_e_ms
rf10_rev_e_ms
rf10_land_e_ss
rf10_rev_e_ss
rf10_land_e_sg
rf10_rev_e_sg
rf10_land_e_dg
rf10_rev_e_dg
rf10_land_e_tf
rf10_rev_e_tf
rf10_land_e_ja
rf10_rev_e_ja
rf10_land_e_tr
rf10_rev_e_tr
rf10_land_e_gp
rf10_rev_e_gp
rf10_land_e_cp
rf10_rev_e_cp
2007-2014
rf10_land_t_2007_2014
rf10_rev_t_2007_2014
rf10_land_t_2015_2021
rf10_rev_t_2015_2021
rf10_land_s_fl
rf10_rev_s_fl
rf10_land_s_al
rf10_rev_s_al
rf10_land_s_ms
rf10_rev_s_ms
rf10_land_s_la
rf10_rev_s_la
rf10_land_s_tx
rf10_rev_s_tx    
    
    
'''