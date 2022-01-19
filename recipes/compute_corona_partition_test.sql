insert into
    "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA_COPY"(
        SELECT
            "iso_code", "date_parsed_formatted"
        FROM
            "PUBLIC"."EVERYTHING_SNOWFLAKE_CORONA"
        GROUP BY
            date_parsed_formatted
    );
