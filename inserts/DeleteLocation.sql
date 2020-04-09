CREATE OR REPLACE FUNCTION DeleteLocation(name_ character varying,
								  river_ character varying) RETURNS VOID AS
$$
BEGIN
    DELETE FROM public.locations where location_river_name=river_ and location_name=name_;
END
$$
  LANGUAGE 'plpgsql';