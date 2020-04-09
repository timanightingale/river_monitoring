CREATE OR REPLACE FUNCTION AddLocation(name_ character varying,
								  river_ character varying,
								  subgroup_id integer,
								longtitude double precision,
									  latitude double precision) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.locations (location_name,
									   location_river_name,
								  location_subgroup_id,
									   location_longtitude,
								 location_latitude) 
									   VALUES (name_ ,
								  river_ ,
								  subgroup_id ,
								longtitude ,
									  latitude );
END
$$
  LANGUAGE 'plpgsql';