select 1 as ogc_fid, st_translate(geom, 0 ,yseries) as geom from
(select generate_series(0,90000, 10000) as yseries,st_translate(geom, xseries ,0) as geom from
(select  generate_series(0, 90000, 10000) as xseries, geom from
(select st_envelope(st_makeline(st_makepoint(1380000,630000),st_makepoint(1390000,640000))) as geom) as t1) as t2) as t3
