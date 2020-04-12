CREATE OR REPLACE FUNCTION Validate(pass_ character varying) RETURNS character varying AS
$$
BEGIN
    select user_login from public.laboratory_users where user_pass=md5(pass_);
END

$$
  LANGUAGE 'plpgsql';