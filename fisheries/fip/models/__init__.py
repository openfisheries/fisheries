# coding: utf-8
from sqlalchemy import ARRAY, Boolean, CheckConstraint, Column, Date, Float, Integer, Numeric, String, Table, Text, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AlSmzPo(Base):
    __tablename__ = 'al_smz_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('al_smz_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(16, 6))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class CobiaNewPo(Base):
    __tablename__ = 'cobia_new_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('cobia_new_po_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(9, 0))
    id = Column(Numeric(9, 0))
    group = Column(String(50))
    zone = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class CountiesEdited(Base):
    __tablename__ = 'counties_edited'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('counties_edited_ogc_fid_seq'::regclass)"))
    statename = Column(String(80))
    countyname = Column(String(80))
    id = Column(Numeric(9, 0))
    county = Column(String(80))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Fedstate(Base):
    __tablename__ = 'fedstate'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('fedstate_ogc_fid_seq'::regclass)"))
    fedstate_ = Column(Numeric(10, 0))
    fedstate_i = Column(Numeric(10, 0))
    mms_region = Column(String(1))
    bdry_type_ = Column(String(2))
    bdry_pt_pr = Column(String(7))
    bdry_aprv_ = Column(String(11))
    block_numb = Column(String(6))
    bdry_name_ = Column(Numeric(5, 0))
    bdry_name1 = Column(String(80))
    bdry_cov_s = Column(Numeric(10, 0))
    wkb_geometry = Column(Geometry('MULTILINESTRING', 4267, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class FgbnmsPy(Base):
    __tablename__ = 'fgbnms_py'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('fgbnms_py_ogc_fid_seq'::regclass)"))
    polygon_id = Column(String(10))
    name = Column(String(20))
    area_sqmi = Column(Numeric(13, 5))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class FlowergardenhapcPo(Base):
    __tablename__ = 'flowergardenhapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('flowergardenhapc_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(16, 6))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class GulfReefllSeasonalPo(Base):
    __tablename__ = 'gulf_reefll_seasonal_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('gulf_reefll_seasonal_po_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(9, 0))
    id = Column(Numeric(9, 0))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class GulfshrimpBycatchPo(Base):
    __tablename__ = 'gulfshrimp_bycatch_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('gulfshrimp_bycatch_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(19, 6))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Hb(Base):
    __tablename__ = 'hb'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('hb_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    vessels = Column(Numeric(9, 0))
    pings = Column(Numeric(9, 0))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Hmssg(Base):
    __tablename__ = 'hmssg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('hmssg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class HmssgSFl(Base):
    __tablename__ = 'hmssg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('hmssg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class HmssgSLa(Base):
    __tablename__ = 'hmssg_s_la'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('hmssg_s_la_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class KingMackerelPo(Base):
    __tablename__ = 'king_mackerel_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('king_mackerel_po_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(9, 0))
    id = Column(Numeric(9, 0))
    group = Column(String(50))
    zone = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class LobsterTrapGearPo(Base):
    __tablename__ = 'lobster_trap_gear_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('lobster_trap_gear_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(6, 0))
    lobster_id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class MadswanSteamboatEdgesPo(Base):
    __tablename__ = 'madswan_steamboat_edges_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('madswan_steamboat_edges_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(16, 6))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class McgrailBankhapcPo(Base):
    __tablename__ = 'mcgrail_bankhapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('mcgrail_bankhapc_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(6, 0))
    area_name = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class MiddlegroundshapcPo(Base):
    __tablename__ = 'middlegroundshapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('middlegroundshapc_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Platform(Base):
    __tablename__ = 'platform'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('platform_ogc_fid_seq'::regclass)"))
    str_number = Column(Numeric(5, 0))
    complex_id = Column(Numeric(10, 0))
    str_name = Column(String(15))
    install_da = Column(Date)
    removal_da = Column(Date)
    wkb_geometry = Column(Geometry('POINT', 4267, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class PplArc(Base):
    __tablename__ = 'ppl_arcs'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('ppl_arcs_ogc_fid_seq'::regclass)"))
    segment_nu = Column(Numeric(10, 0))
    seg_length = Column(Numeric(10, 0))
    status_cod = Column(String(4))
    ppl_size_c = Column(String(6))
    row_number = Column(String(8))
    prod_code = Column(String(4))
    aprv_code = Column(String(1))
    sde_compan = Column(String(100))
    shape_leng = Column(Numeric(19, 11))
    wkb_geometry = Column(Geometry('MULTILINESTRING', 4267, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class PulleyRidgehapcPo(Base):
    __tablename__ = 'pulley_ridgehapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('pulley_ridgehapc_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(6, 0))
    area_name = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


t_raster_columns = Table(
    'raster_columns', metadata,
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('srid', Integer),
    Column('scale_x', Float(53)),
    Column('scale_y', Float(53)),
    Column('blocksize_x', Integer),
    Column('blocksize_y', Integer),
    Column('same_alignment', Boolean),
    Column('regular_blocking', Boolean),
    Column('num_bands', Integer),
    Column('pixel_types', ARRAY(Text())),
    Column('nodata_values', ARRAY(Float(precision=53))),
    Column('out_db', ARRAY(Boolean())),
    Column('extent', Geometry(spatial_index=False, from_text='ST_GeomFromEWKT', name='geometry')),
    Column('spatial_index', Boolean)
)


t_raster_overviews = Table(
    'raster_overviews', metadata,
    Column('o_table_catalog', String),
    Column('o_table_schema', String),
    Column('o_table_name', String),
    Column('o_raster_column', String),
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('overview_factor', Integer)
)


class ReeffishTerritoriesLocoh(Base):
    __tablename__ = 'reeffish_territories_locoh'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('reeffish_territories_locoh_ogc_fid_seq'::regclass)"))
    sp_id = Column(String(5))
    id = Column(Numeric(5, 0))
    county = Column(String(15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Rf10LandESpecy(Base):
    __tablename__ = 'rf10_land_e_species'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000245E59410000000020293B4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E59410000000020293B4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 171')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_e_species_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandSAl(Base):
    __tablename__ = 'rf10_land_s_al'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000A0613C4100000000EC0D5A4100000000A0613C4100000000184E5C410000000020B8484100000000184E5C410000000020B8484100000000EC0D5A4100000000A0613C4100000000EC0D5A41'::geometry"),
        CheckConstraint('st_height(rast) = 59'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000A0613C4100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 138')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_s_al_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandSFl(Base):
    __tablename__ = 'rf10_land_s_fl'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000A0613C4100000000245E594100000000A0613C4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E594100000000A0613C4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000A0613C4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 163')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_s_fl_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandSLa(Base):
    __tablename__ = 'rf10_land_s_la'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000080133C410000000084485A410000000080133C4100000000184E5C4100000000D840494100000000184E5C4100000000D84049410000000084485A410000000080133C410000000084485A41'::geometry"),
        CheckConstraint('st_height(rast) = 53'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000080133C4100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 147')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_s_la_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandSM(Base):
    __tablename__ = 'rf10_land_s_ms'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000889B4341000000009CBB5B4100000000889B434100000000184E5C410000000008D4444100000000184E5C410000000008D44441000000009CBB5B4100000000889B4341000000009CBB5B41'::geometry"),
        CheckConstraint('st_height(rast) = 15'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000889B434100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 16')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_s_ms_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandSTx(Base):
    __tablename__ = 'rf10_land_s_tx'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000C03E5A410000000020293B4100000000903A5C4100000000B035454100000000903A5C4100000000B035454100000000C03E5A410000000020293B4100000000C03E5A41'::geometry"),
        CheckConstraint('st_height(rast) = 52'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000903A5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 100')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_s_tx_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandT20072014(Base):
    __tablename__ = 'rf10_land_t_2007_2014'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000245E59410000000020293B4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E59410000000020293B4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 171')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_t_2007_2014_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10LandT20152021(Base):
    __tablename__ = 'rf10_land_t_2015_2021'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000030503B410000000064FA59410000000030503B4100000000646B5C410000000058794A4100000000646B5C410000000058794A410000000064FA59410000000030503B410000000064FA5941'::geometry"),
        CheckConstraint('st_height(rast) = 64'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000030503B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 168')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_land_t_2015_2021_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevESpecy(Base):
    __tablename__ = 'rf10_rev_e_species'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000245E59410000000020293B4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E59410000000020293B4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 171')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_e_species_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevSAl(Base):
    __tablename__ = 'rf10_rev_s_al'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000A0613C4100000000EC0D5A4100000000A0613C4100000000184E5C410000000020B8484100000000184E5C410000000020B8484100000000EC0D5A4100000000A0613C4100000000EC0D5A41'::geometry"),
        CheckConstraint('st_height(rast) = 59'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000A0613C4100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 138')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_s_al_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevSFl(Base):
    __tablename__ = 'rf10_rev_s_fl'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000A0613C4100000000245E594100000000A0613C4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E594100000000A0613C4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000A0613C4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 163')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_s_fl_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevSLa(Base):
    __tablename__ = 'rf10_rev_s_la'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000080133C410000000084485A410000000080133C4100000000184E5C4100000000D840494100000000184E5C4100000000D84049410000000084485A410000000080133C410000000084485A41'::geometry"),
        CheckConstraint('st_height(rast) = 53'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000080133C4100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 147')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_s_la_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevSM(Base):
    __tablename__ = 'rf10_rev_s_ms'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C0000010000000500000000000000889B4341000000009CBB5B4100000000889B434100000000184E5C410000000008D4444100000000184E5C410000000008D44441000000009CBB5B4100000000889B4341000000009CBB5B41'::geometry"),
        CheckConstraint('st_height(rast) = 15'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C000000000889B434100000000184E5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 16')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_s_ms_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevSTx(Base):
    __tablename__ = 'rf10_rev_s_tx'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000C03E5A410000000020293B4100000000903A5C4100000000B035454100000000903A5C4100000000B035454100000000C03E5A410000000020293B4100000000C03E5A41'::geometry"),
        CheckConstraint('st_height(rast) = 52'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000903A5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 100')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_s_tx_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevT20072014(Base):
    __tablename__ = 'rf10_rev_t_2007_2014'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000020293B4100000000245E59410000000020293B4100000000646B5C410000000068A04A4100000000646B5C410000000068A04A4100000000245E59410000000020293B4100000000245E5941'::geometry"),
        CheckConstraint('st_height(rast) = 80'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000020293B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 171')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_t_2007_2014_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rf10RevT20152021(Base):
    __tablename__ = 'rf10_rev_t_2015_2021'
    __table_args__ = (
        CheckConstraint("_raster_constraint_nodata_values(rast) = '{-339999995214436000000000000000000000000.0000000000}'::numeric[]"),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('round((st_scalex(rast))::numeric, 10) = round((10000)::numeric, 10)'),
        CheckConstraint('round((st_scaley(rast))::numeric, 10) = round((- (10000)::numeric), 10)'),
        CheckConstraint("st_envelope(rast) @ '01030000200B0C000001000000050000000000000030503B410000000064FA59410000000030503B4100000000646B5C410000000058794A4100000000646B5C410000000058794A410000000064FA59410000000030503B410000000064FA5941'::geometry"),
        CheckConstraint('st_height(rast) = 64'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint("st_samealignment(rast, '0100000000000000000088C340000000000088C3C00000000030503B4100000000646B5C41000000000000000000000000000000000B0C000001000100'::raster)"),
        CheckConstraint('st_srid(rast) = 3083'),
        CheckConstraint('st_width(rast) = 168')
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('rf10_rev_t_2015_2021_rid_seq'::regclass)"))
    rast = Column(Raster(from_text='raster', name='raster'), index=True)


class Rfbsg(Base):
    __tablename__ = 'rfbsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfbsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    lnd__ms = Column(Numeric(24, 15))
    rev__ms = Column(Numeric(24, 15))
    lnd__ss = Column(Numeric(24, 15))
    rev__ss = Column(Numeric(24, 15))
    lnd__sg = Column(Numeric(24, 15))
    rev__sg = Column(Numeric(24, 15))
    lnd__dg = Column(Numeric(24, 15))
    rev__dg = Column(Numeric(24, 15))
    lnd__tf = Column(Numeric(24, 15))
    rev__tf = Column(Numeric(24, 15))
    lnd__ja = Column(Numeric(24, 15))
    rev__ja = Column(Numeric(24, 15))
    lnd__tr = Column(Numeric(24, 15))
    rev__tr = Column(Numeric(24, 15))
    lnd__gp = Column(Numeric(24, 15))
    rev__gp = Column(Numeric(24, 15))
    lnd__cp = Column(Numeric(24, 15))
    rev__cp = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfbsgSFl(Base):
    __tablename__ = 'rfbsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfbsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfbsgT20072014(Base):
    __tablename__ = 'rfbsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfbsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfbsgT20152021(Base):
    __tablename__ = 'rfbsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfbsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Rfdsg(Base):
    __tablename__ = 'rfdsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfdsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    lnd__ms = Column(Numeric(24, 15))
    rev__ms = Column(Numeric(24, 15))
    lnd__ss = Column(Numeric(24, 15))
    rev__ss = Column(Numeric(24, 15))
    lnd__sg = Column(Numeric(24, 15))
    rev__sg = Column(Numeric(24, 15))
    lnd__dg = Column(Numeric(24, 15))
    rev__dg = Column(Numeric(24, 15))
    lnd__tf = Column(Numeric(24, 15))
    rev__tf = Column(Numeric(24, 15))
    lnd__ja = Column(Numeric(24, 15))
    rev__ja = Column(Numeric(24, 15))
    lnd__tr = Column(Numeric(24, 15))
    rev__tr = Column(Numeric(24, 15))
    lnd__gp = Column(Numeric(24, 15))
    rev__gp = Column(Numeric(24, 15))
    lnd__cp = Column(Numeric(24, 15))
    rev__cp = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfdsgSFl(Base):
    __tablename__ = 'rfdsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfdsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfdsgT20072014(Base):
    __tablename__ = 'rfdsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfdsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfdsgT20152021(Base):
    __tablename__ = 'rfdsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfdsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Rfgnsg(Base):
    __tablename__ = 'rfgnsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfgnsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    lnd__ms = Column(Numeric(24, 15))
    rev__ms = Column(Numeric(24, 15))
    lnd__ss = Column(Numeric(24, 15))
    rev__ss = Column(Numeric(24, 15))
    lnd__sg = Column(Numeric(24, 15))
    rev__sg = Column(Numeric(24, 15))
    lnd__dg = Column(Numeric(24, 15))
    rev__dg = Column(Numeric(24, 15))
    lnd__tf = Column(Numeric(24, 15))
    rev__tf = Column(Numeric(24, 15))
    lnd__ja = Column(Numeric(24, 15))
    rev__ja = Column(Numeric(24, 15))
    lnd__tr = Column(Numeric(24, 15))
    rev__tr = Column(Numeric(24, 15))
    lnd__gp = Column(Numeric(24, 15))
    rev__gp = Column(Numeric(24, 15))
    lnd__cp = Column(Numeric(24, 15))
    rev__cp = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfgnsgSFl(Base):
    __tablename__ = 'rfgnsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfgnsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfgnsgT20072014(Base):
    __tablename__ = 'rfgnsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfgnsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfgnsgT20152021(Base):
    __tablename__ = 'rfgnsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfgnsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Rfsg(Base):
    __tablename__ = 'rfsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    lnd__ms = Column(Numeric(24, 15))
    rev__ms = Column(Numeric(24, 15))
    lnd__ss = Column(Numeric(24, 15))
    rev__ss = Column(Numeric(24, 15))
    lnd__sg = Column(Numeric(24, 15))
    rev__sg = Column(Numeric(24, 15))
    lnd__dg = Column(Numeric(24, 15))
    rev__dg = Column(Numeric(24, 15))
    lnd__tf = Column(Numeric(24, 15))
    rev__tf = Column(Numeric(24, 15))
    lnd__ja = Column(Numeric(24, 15))
    rev__ja = Column(Numeric(24, 15))
    lnd__tr = Column(Numeric(24, 15))
    rev__tr = Column(Numeric(24, 15))
    lnd__gp = Column(Numeric(24, 15))
    rev__gp = Column(Numeric(24, 15))
    lnd__cp = Column(Numeric(24, 15))
    rev__cp = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgSAl(Base):
    __tablename__ = 'rfsg_s_al'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_s_al_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgSFl(Base):
    __tablename__ = 'rfsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgSLa(Base):
    __tablename__ = 'rfsg_s_la'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_s_la_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgSM(Base):
    __tablename__ = 'rfsg_s_ms'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_s_ms_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgSTx(Base):
    __tablename__ = 'rfsg_s_tx'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_s_tx_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgT20072014(Base):
    __tablename__ = 'rfsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RfsgT20152021(Base):
    __tablename__ = 'rfsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rfsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Rftsg(Base):
    __tablename__ = 'rftsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    lnd__ms = Column(Numeric(24, 15))
    rev__ms = Column(Numeric(24, 15))
    lnd__ss = Column(Numeric(24, 15))
    rev__ss = Column(Numeric(24, 15))
    lnd__sg = Column(Numeric(24, 15))
    rev__sg = Column(Numeric(24, 15))
    lnd__dg = Column(Numeric(24, 15))
    rev__dg = Column(Numeric(24, 15))
    lnd__tf = Column(Numeric(24, 15))
    rev__tf = Column(Numeric(24, 15))
    lnd__ja = Column(Numeric(24, 15))
    rev__ja = Column(Numeric(24, 15))
    lnd__tr = Column(Numeric(24, 15))
    rev__tr = Column(Numeric(24, 15))
    lnd__gp = Column(Numeric(24, 15))
    rev__gp = Column(Numeric(24, 15))
    lnd__cp = Column(Numeric(24, 15))
    rev__cp = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RftsgSAl(Base):
    __tablename__ = 'rftsg_s_al'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_s_al_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RftsgSFl(Base):
    __tablename__ = 'rftsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RftsgSLa(Base):
    __tablename__ = 'rftsg_s_la'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_s_la_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RftsgT20072014(Base):
    __tablename__ = 'rftsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class RftsgT20152021(Base):
    __tablename__ = 'rftsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rftsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Sfsg(Base):
    __tablename__ = 'sfsg'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    lnd__bs = Column(Numeric(24, 15))
    rev__bs = Column(Numeric(24, 15))
    lnd__ws = Column(Numeric(24, 15))
    rev__ws = Column(Numeric(24, 15))
    land__s = Column(Numeric(24, 15))
    rev_e_s = Column(Numeric(24, 15))
    lnd__rs = Column(Numeric(24, 15))
    rev__rs = Column(Numeric(24, 15))
    land__t = Column(Numeric(24, 15))
    rev_e_t = Column(Numeric(24, 15))
    lnd__ps = Column(Numeric(24, 15))
    rev__ps = Column(Numeric(24, 15))
    ln__rrs = Column(Numeric(24, 15))
    rv__rrs = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgSAl(Base):
    __tablename__ = 'sfsg_s_al'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_s_al_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgSFl(Base):
    __tablename__ = 'sfsg_s_fl'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_s_fl_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgSLa(Base):
    __tablename__ = 'sfsg_s_la'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_s_la_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgSM(Base):
    __tablename__ = 'sfsg_s_ms'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_s_ms_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgSTx(Base):
    __tablename__ = 'sfsg_s_tx'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_s_tx_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgT20072014(Base):
    __tablename__ = 'sfsg_t_2007_2014'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_t_2007_2014_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SfsgT20152021(Base):
    __tablename__ = 'sfsg_t_2015_2021'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('sfsg_t_2015_2021_ogc_fid_seq'::regclass)"))
    sz_id = Column(String(80))
    lnd_vrl = Column(Numeric(24, 15))
    rv_vrll = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShapefileRecrSwgLnGomxSero(Base):
    __tablename__ = 'shapefile_recr_swg_ln_gomx_sero'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shapefile_recr_swg_ln_gomx_sero_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(16, 6))
    descriptio = Column(String(50))
    wkb_geometry = Column(Geometry('MULTILINESTRING', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShapefileReefFishLonglineBuoyGearPoGomxSero(Base):
    __tablename__ = 'shapefile_reef_fish_longline_buoy_gear_po_gomx_sero'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shapefile_reef_fish_longline_buoy_gear_po_gomx_sero_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShapefileReefFishStressedPoGomxSero(Base):
    __tablename__ = 'shapefile_reef_fish_stressed_po_gomx_sero'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shapefile_reef_fish_stressed_po_gomx_sero_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShippingFairway(Base):
    __tablename__ = 'shipping_fairways'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shipping_fairways_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(5, 0))
    themelayer = Column(String(40))
    inform = Column(String(250))
    objnam = Column(String(57))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShrimpAllyearsKde(Base):
    __tablename__ = 'shrimp_allyears_kde'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shrimp_allyears_kde_ogc_fid_seq'::regclass)"))
    sp_id = Column(String(5))
    id = Column(Numeric(5, 0))
    county = Column(String(15))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class ShrimpCrabPo(Base):
    __tablename__ = 'shrimp_crab_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('shrimp_crab_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    zone = Column(String(30))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SpanishMackerelPo(Base):
    __tablename__ = 'spanish_mackerel_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('spanish_mackerel_po_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(9, 0))
    id = Column(Numeric(9, 0))
    group = Column(String(50))
    zone = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class StetsonBankhapcPo(Base):
    __tablename__ = 'stetson_bankhapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('stetson_bankhapc_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(6, 0))
    area_name = Column(String(50))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class SwflSeasonalPo(Base):
    __tablename__ = 'swfl_seasonal_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('swfl_seasonal_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class TexasExceptPo(Base):
    __tablename__ = 'texas_except_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('texas_except_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class TexasPo(Base):
    __tablename__ = 'texas_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('texas_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class TortugasShrimpPo(Base):
    __tablename__ = 'tortugas_shrimp_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('tortugas_shrimp_po_ogc_fid_seq'::regclass)"))
    label = Column(String(50))
    id = Column(Numeric(16, 6))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class TortugasmrHapcPo(Base):
    __tablename__ = 'tortugasmr_hapc_po'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('tortugasmr_hapc_po_ogc_fid_seq'::regclass)"))
    id = Column(Numeric(16, 6))
    label = Column(String(50))
    wkb_geometry = Column(Geometry('MULTIPOLYGON', 4269, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class Usmaritimelimitsnboundary(Base):
    __tablename__ = 'usmaritimelimitsnboundaries'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('usmaritimelimitsnboundaries_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(10, 0))
    bound_id = Column(String(5))
    region = Column(String(100))
    feat_type = Column(String(100))
    pub_date = Column(Date)
    apprv_date = Column(Date)
    legal_auth = Column(String(100))
    aor = Column(String(20))
    note = Column(String(254))
    supp_info = Column(String(254))
    ts = Column(Numeric(19, 8))
    cz = Column(Numeric(19, 8))
    eez = Column(Numeric(19, 8))
    f_eez = Column(Numeric(19, 8))
    symbol = Column(Numeric(19, 8))
    unilateral = Column(Numeric(19, 8))
    wkb_geometry = Column(Geometry('MULTILINESTRING', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)


class WaterwayNetwork(Base):
    __tablename__ = 'waterway_network'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('waterway_network_ogc_fid_seq'::regclass)"))
    objectid = Column(Numeric(4, 0))
    id = Column(Numeric(6, 0))
    length = Column(Numeric(24, 15))
    dir = Column(Numeric(1, 0))
    linknum = Column(Numeric(24, 15))
    anode = Column(Numeric(6, 0))
    bnode = Column(Numeric(6, 0))
    linkname = Column(String(35))
    rivername = Column(String(35))
    amile = Column(Numeric(24, 15))
    bmile = Column(Numeric(24, 15))
    length1 = Column(Numeric(24, 15))
    length_src = Column(String(1))
    shape_src = Column(String(3))
    linktype = Column(String(10))
    ctrl_depth = Column(Numeric(3, 0))
    waterway = Column(String(4))
    geo_class = Column(String(1))
    func_class = Column(String(1))
    wtwy_type = Column(Numeric(2, 0))
    chart_id = Column(String(15))
    num_pairs = Column(Numeric(3, 0))
    who_mod = Column(String(3))
    date_mod = Column(String(8))
    heading = Column(String(1))
    state = Column(String(2))
    fips = Column(String(2))
    fips2 = Column(String(2))
    non_us = Column(String(2))
    key_id = Column(String(20))
    wtwy_uniq = Column(String(12))
    min_meas = Column(Numeric(24, 15))
    max_meas = Column(Numeric(24, 15))
    shape_leng = Column(Numeric(24, 15))
    wkb_geometry = Column(Geometry('MULTILINESTRING', 4326, from_text='ST_GeomFromEWKT', name='geometry'), index=True)
