CREATE TABLE sign
(
    name TEXT NOT NULL,
    sid TEXT NOT NULL,
    cid TEXT NOT NULL,
    date DATE NOT NULL
);
CREATE INDEX sign_sid_index ON sign (sid);
CREATE INDEX sign_cid_index ON sign (cid)