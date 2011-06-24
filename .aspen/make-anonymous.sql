UPDATE cdr
SET dstchannel='SIP/' + dst,
channel='SIP/' + src,
lastdata = '';

UPDATE cdr
SET dst = abs(random())
WHERE length(dst) > 3;

UPDATE cdr
SET src = abs(random())
WHERE length(src) > 3;

UPDATE cdr
SET clid = '"' || src || '"' || ' <' || src || '>';

