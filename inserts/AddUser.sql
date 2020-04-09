CREATE OR REPLACE FUNCTION AddUser(first_name character varying,
								  last_name character varying,
								  email character varying) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.laboratory_logs (user_first_name,
									   user_last_name,
									   email) 
									   VALUES (first_name,last_name,email);
END
$$
  LANGUAGE 'plpgsql';