create or replace function public.valid_date(p_str varchar(50))
returns boolean as $$
begin
    perform p_str::date;
    return true;
    exception when others then
    return false;
end;
$$ language plpgsql;