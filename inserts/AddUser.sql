CREATE OR REPLACE FUNCTION AddUser(first_name character varying,
								  last_name character varying,
								  email character varying,
								  pass_ character varying,
								  login_ character varying) RETURNS VOID AS
$$
BEGIN
    INSERT INTO public.laboratory_users (user_id,
										user_first_name,
									   user_last_name,
									   user_email,
										user_pass,
										user_login) 
									   VALUES (
										(select max(user_id)+1 from public.laboratory_users),   
										   first_name,last_name,email,md5(pass_),login_);
END

$$
  LANGUAGE 'plpgsql';