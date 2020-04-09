CREATE OR REPLACE FUNCTION AddOrganisationLocation(org_id integer,loc_id integer) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.organisation_locations (organisation_id, location_id) 
									   VALUES (org_id ,loc_id);
END
$$
  LANGUAGE 'plpgsql';