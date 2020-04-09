CREATE OR REPLACE FUNCTION AddOrganisationVals(org_id integer,
								  loc_id integer, indicator_id integer, category double precision) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.organisation_values (organisation_id, location_id, indicator_id, category_permited) 
									   VALUES (org_id,
								  loc_id, indicator_id, category);
END
$$
  LANGUAGE 'plpgsql';