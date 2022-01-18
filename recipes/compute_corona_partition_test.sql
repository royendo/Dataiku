 delete from
    "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA"
where
    date_parsed_formatted like '2021-%' ;commit;
insert into
    "EVERYTHING_CORONA_PARTITION_TEST"(
        SELECT
            *
        FROM
            "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA"
        GROUP BY
            date_parsed_formatted
    );
