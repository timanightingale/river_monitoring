CREATE OR REPLACE FUNCTION Validate(pass_ character varying) RETURNS character varying AS $$
declare login_ character varying;
begin
    select nth_value(user_login,1) over(order by user_id) 
	into login_ 
	from public.laboratory_users 
	where user_pass=md5(pass_);
	return login_;
end;
$$
  LANGUAGE 'plpgsql';