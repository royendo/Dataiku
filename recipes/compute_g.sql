SELECT
  CASE
    WHEN
      "EVERYTHING_single_copy_copy".flag = '0'
        THEN
          '1'
  END AS flag,
  "EVERYTHING_single_copy_copy".*
FROM
  "EVERYTHING_single_copy_copy"