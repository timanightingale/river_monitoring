CREATE OR REPLACE FUNCTION AddOrganisation(name_ character varying,
								  email character varying) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.organisation_names (organisation_name, organisation_email) 
									   VALUES (name_ ,
								  email);
END
$$
  LANGUAGE 'plpgsql';