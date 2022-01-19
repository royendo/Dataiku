insert into
    "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA_COPY"(
        SELECT
            *
        FROM
            "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA"
        GROUP BY
            date_parsed_formatted
    );
