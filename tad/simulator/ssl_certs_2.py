from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUbFhRlgpIM3M+ZYuTigQ1Vbmi6P4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyMloXDTMyMDMy
MDE3MjkyMlowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAsc4R76dCSzj3MR7adSLI+Mk9cX42bTHiu00c964rUXr2
eGpYy1fmtdiq71kkVFRCtX+m8tc0jA5RCOCJsVKPZ7a2zQVcUkC1HJDCg8lufI2p
hS33zpjP+BePGmxQDhBU744cmFA/TVN+VTEhTlbmhFo62eX2Repbl2coF3MhoKTz
cilUgiCww+DUa6IQk06Zkh8TFJ8iPp67QRM1wEhMEcKrnRNxPGHDxa9ZxhwrmKft
UOFrat+ijftQDexMkVZLUXPoksM/7afjqvP9fkFpQEJZ3R1p3uwSX+oIr4yE/0il
nnLnunvUcWYTmvVcwrV5Zu+IOtV+yBbJxmFsobiecQIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQAgxl6fGre+yFpKxEVcJ554klsg
Hefei1tv94BDMqdzfdeocTBiYmN70j9KEZr5CoMUhpRh0sESpgZ+6JD506Crpa6y
CwkhfQXwOH58E6pbqLLpG3F96BeIBQ/IS0iGvRaerK/9hybt4NJAyrXX1idJikiJ
h4qck731LOSiCw7T138yjlVEXm4DdCj/MYJDJJznMYDXJrJEE7tDHHvPaPU3Snrd
CeAYwXaZlvoCbU0f0DCyAXS5+/HgzY5qVrvDTADTAEnMSEQyIhESSL2xmumTGNCA
BBlbMJ6oLn3fOHrB7qQortCwcAQkbk/MiZhAkL/+NDz6gdIZqgXLDDVZxext
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsc4R76dCSzj3MR7adSLI+Mk9cX42bTHiu00c964rUXr2eGpY
y1fmtdiq71kkVFRCtX+m8tc0jA5RCOCJsVKPZ7a2zQVcUkC1HJDCg8lufI2phS33
zpjP+BePGmxQDhBU744cmFA/TVN+VTEhTlbmhFo62eX2Repbl2coF3MhoKTzcilU
giCww+DUa6IQk06Zkh8TFJ8iPp67QRM1wEhMEcKrnRNxPGHDxa9ZxhwrmKftUOFr
at+ijftQDexMkVZLUXPoksM/7afjqvP9fkFpQEJZ3R1p3uwSX+oIr4yE/0ilnnLn
unvUcWYTmvVcwrV5Zu+IOtV+yBbJxmFsobiecQIDAQABAoIBABilM59AU9QRZVIN
sMIjvC+f1UBx+iFQlNjZa3Z5Uc/Nd3RhaUVmPbhe+/KJLJvzwfteYkmuwr3XDixo
0y0dAHuju9rXL2DHT1NSTWPu+72P9Ttcj8i3Lbx5p4BGGyKX6O37iMMj/GI/fHda
g/9T1EfsKdQiJ+yw+1kVF12Iu9SETXVSl+xtEv0D0nj3vvSCzHf3wPELNMDigb1k
R43zsbzT/QF03rlMy22xkNWDyxki1EdmkuU93+8DQCso5r5OwI3hGDQzWW2c5nPm
49+m7lHe3apYUxjhbdLAWfyviEI5ysIhf9qwRXZJTHj7qncrkYZMm4wI49TWb318
Sw/EwnECgYEA3021Gg6lqwfL3++mUKYyGEKVwRFPK9cZU6+xMT+yjPtahnbRlueL
pZ/rRYKUe5iIGYNdHoQgLqsE9hh0iZbjiNLQ0HLvMBt0QdMey+F6vKlzkSiBJsmf
mZXgQMI36uHbuJcm9Dm/nSoxQT0rmHk1rdW0hpJZOtUKMlm1SdjUH+8CgYEAy9bl
tTyq8oMwXJ7dp3UfLtSL4y5ekPLe8o+/cMTOHjaZBDFdPXgFN3DQLqrhvPAQHl1G
PI+zsjLoZYBtrOgIJ0Dt/4N9jijSdfhfZtwpXcVxWPXSjh/hTmY29pD3IDV9sbyq
PyLxpMaCL8BrUXPTpLyuuUUpanPxhzG5FXs6x58CgYEAtruiXcZqr8Dbh09XbFv0
VoH2hl2hyiBla2Q0vjZ/6HqwI6UL8k9cqZZqMyGeXF3/0dD73MMGiuoMT07H3ugJ
HqhVlJ7ZOSbeRhd79h94DvcjyT+6IIGSB17selH07FMTOMUIbYbsVLJ4SAjEqitW
UAC3kAAm4MwBYh6jCeFUBSUCgYAkuSeTOkXWARqSZTCrvacLidFV8YGp/Yd7DbjA
uUQlH1L79WTF8TyHW3S2I6Udo+ZTghxoRr9qCE/kEXow33CwmbsHAIp7NRGNnVya
rGlrcmnUTB1N66JsvG+EhmNvUxO9FK9bRpFgTT8hGTp8ZzCnCjM0P6iRfCf0Ylnk
69mQIwKBgQC0lu/wkUsJtbMaUDW5v05XoVw3c+aHd3fFX7WW10d4aDqzFXYMjdxT
tKpkYxpBuoco9E1PZMF248wGMsIltykwPvy7QI3gRbsZIW6gTwUBsI3xTYOybu2x
trfVO6ksP0sIoYOJH2JbJfIyzy49hA90x1cIA7i/HdJWRGitJ/xKkw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUJBzmO7OHvvlimGi0mXLrh/8TPeMwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC792uVfc1mFbJluKxzWxZ0r5yaKGjR8azECVrNTcegAjLF
Qd7+iZS+7DZwEA6Xy/h8T9DZd3Q1m0Rjlgg73ngO50leCvLqWEvrhueuEIWLdbef
4NaX4qkusMI/orYE/ItKgL86HWkGUELnmf3TkMccohR63vS+Fr6dZDvIw3g+gBPL
P9MlK7sdXq1I8CIcV+2du4jhmkA4mJ278TdQZOfXnX1hhe1wPuyhJyBN1sV2ntLG
TLcRl8WQSIh3j4vhMilEU85rA+q4TuqrOlZtKPTPNGeACwrD7qQkWihsEAKWMdQJ
e++9+CdigL/S3IhMmdTwHHNht31oYl1vAqbQbCEzAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAttszf/gjwRvkxZs8Iq474
aoBzfsF/NKCKBNRoTdVwQc6DycJylA9JL45BFhc39tka00ttcKGbXmbnOzltnFsH
QuD/1B4pQOESZzUEcsHHCn7tKxIrCn4wk9OiiqcIwHwavFy+guHFSw71jVFhv6im
ILe/K+wzpgc+pUeYiQlWRSuoR7YABZekL8bjpCpuq1kXzP4bV9pnq0sMayCHdH+q
enRnvo4u6PtMUGdX+bye3sp609uFgH53v06ufl3ylkoK5TRuaOj84yYuJDBrAAG6
ZYZaosM/CKXoumetH90Sc2rAvWp2HniHe99STfaw1aNK9YV1T9SjIqhzyzoMzGRP
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAu/drlX3NZhWyZbisc1sWdK+cmiho0fGsxAlazU3HoAIyxUHe
/omUvuw2cBAOl8v4fE/Q2Xd0NZtEY5YIO954DudJXgry6lhL64bnrhCFi3W3n+DW
l+KpLrDCP6K2BPyLSoC/Oh1pBlBC55n905DHHKIUet70vha+nWQ7yMN4PoATyz/T
JSu7HV6tSPAiHFftnbuI4ZpAOJidu/E3UGTn1519YYXtcD7soScgTdbFdp7Sxky3
EZfFkEiId4+L4TIpRFPOawPquE7qqzpWbSj0zzRngAsKw+6kJFoobBACljHUCXvv
vfgnYoC/0tyITJnU8BxzYbd9aGJdbwKm0GwhMwIDAQABAoIBABntdxmX0M1UENeX
MbJ3zhEqaB+bk1niTEJ+R9gp8m9P3lD3VRsnPy1Wx+uNS3YE3LHJELXulEkQsc5K
07fuaAEmRiiCuh85Lr++TBbmkIU8J6gWC4PH8C5Qk3rTpufpLg2I1NffVq1YROJN
i4WzYsPAV7LbLkdKO+DaAqUe0WdNZph8Fhrg/WhjGC5VAajRgfVM7cbnW4SjrQzz
lqoVB3GQPWLgUhHoBj6yRMBKP7D96h+oqUZprn19ilEeaoDVvDMx1Uqj57PGCZ8k
c166dctWvSVxLKwbau20HLAZCZWQylhOugk3sEIceEhkiP95LYNfAZAHiU1Aqfpe
PgKSAYECgYEA8uvqkXwejuFEMGJWo/JUH/pETc420gatwVD222LYYFeNhk3C6k/E
iHa/iE8v9jKHTv7xmlG6ybBkluDGsaK2vngzKpc97nCYfg3mFjS3CN/leZDMwUDX
Bj1XgFhYM9yLVojwVJl3PkA4B/WYmnxgSo9u9oCy9K8HdSMUcCcPQgcCgYEAxhYU
9OPA0VmKYwipWfpZlir5LrvLkwJdcmAV5UhKVXkMXr+M9ByRRLYrr++6SxipjOjO
Zi1t1hB79pxtc2mFBCT9gtnbNvcgEdkxSo08U/uj3xcp1oCZAN9Vu3Dk19Oi3jUT
BAlE1V+Le3b0mPh9IytPjpO7xjWstpi5ar6obHUCgYAH0x+QJh5Z3dmzcUd3KnQZ
P5d5ph3P8BUit/froyhzGf7eB50yrPUYrDKJMnvKA2CmY8HmhaFto7fpwD3GNQaL
5hVH1u1Qw+G1lb8GkhYfPA8JNmfSBcOnWMx7vtzAducqF2keYH8dyzXC099hgoYb
gLlDSWv6Q7UKyeF7p1ZvewKBgCnWbCK1H/qXoOT95Vb9y4IuHWdDfuHT9Ay+QqGk
vR6EbJpudsTwa7ZJi7yjM4O898KtQTrPiY1W+ffCXlOsC84uSeUjQmu/kmRyrTiD
0CQk2B28dLe7fZVzllX6qDr1lka8iwGlO4adoYY4P703bqbI9Qq2JUjd+VavtynW
jxgpAoGALXc4mrAJl4ckfso2OOXo0UHYuO7XCVO3Ll5bzGZbaiRuCYG6ilm2wKRf
FnrYRd9KtvrA100LxTTepdo0tTVcdAWY7STJpBIycUN72OMQOCI3VWSTkSpJHGjp
WBqJDcueUhUe8x5//qsMtXJFgXc2ZerODemObr+bRT1nBYMiZQI=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUF2mq+KA3KYyp6bso3F79MnD6AacwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC5wiF41CixaxHM2oHf3nYkuGmLeG6xBdSogQuaSMAw6KCy
AvCfLDBRgfbvWjXV5teUv61+xgyLctNLmJQBg0owYQhhZnwIZK2jK9h5CvquI9UC
xAdgtvKc6yFKlWS435xSt+ja2w5eHsE0QE6U9SL9qm7OnehvF0baDA7CjQNKQ8SR
lkrl0+mQZCEc5lfroYlpOJ1XKrmLhfX4KV+RcNEuLF4roY1TdkUfCOk9Jq8/DrCD
rAOuFaU/GShqmG9REt3HKIGBO254/xoTcSkGIOHOGI/2uZI0MVUDK8tNDwAaDLcg
RAclaoGQ1++jcjnmjvopsqySEJwJrDJMkpqKd0SzAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCImPY2TwUGre7AM6nzBqrh
WCXTEct84E1jfJtgWZ5xYdVMNd0Ujg6A89LZnc//KW1xVDImmTrsxwHj/vR7lRdr
L7ADGbKOepqKMgUdT8Im67jpMen9Bnrx/q5dtW8qmUMc+EpGwvMOASYEa5jxQ1Uy
Bxpyk3lpeZs5HZJPG0WVFQnNXtlG8LMlmlj1JAEB79hbK7PqPvat6rnS6NTCHGtC
vjAd8mHjVQJkla6u4dV4oI+niEJk12d1yJ9dMSZ8hO3CiBJBieZJ2v2S04N8UUMh
PQEX/yYT94hLaYWYextZRDxNWnjS68Ju1xv8j8GKdMLE693Z6K5kJkspBy0sEtxk
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAucIheNQosWsRzNqB3952JLhpi3husQXUqIELmkjAMOigsgLw
nywwUYH271o11ebXlL+tfsYMi3LTS5iUAYNKMGEIYWZ8CGStoyvYeQr6riPVAsQH
YLbynOshSpVkuN+cUrfo2tsOXh7BNEBOlPUi/apuzp3obxdG2gwOwo0DSkPEkZZK
5dPpkGQhHOZX66GJaTidVyq5i4X1+ClfkXDRLixeK6GNU3ZFHwjpPSavPw6wg6wD
rhWlPxkoaphvURLdxyiBgTtueP8aE3EpBiDhzhiP9rmSNDFVAyvLTQ8AGgy3IEQH
JWqBkNfvo3I55o76KbKskhCcCawyTJKaindEswIDAQABAoIBAAWr8LuwtqFcJIn9
rfN45mCOpOJWRgLvq6ONdR471Gpp3+YvgstJXRxP/IsoVPZ3+uMWyyRQxbdIRT1M
plA5gv1hKRFYQLc847RUtWJUvHyuqWVROOxyCYxS/Yw6bX3bjflUli6Ae7rR85I1
2HBh37ShDIsQdTVXH5muvpCgH5aX18gONUYsQt+xDbnuDW1Cdl6MFYCNCOzL1W5k
6kccejG2aDvNN4f9FZdtvft4sQFp61LGxClZGml9zlFuOav/dJx3eXU47Z8DVADw
OJmtXJend7A29uPFyyoQ44uE0F1SG0dzNmmrxrD39c90w3BTvyGsilmjkr1diRkv
jRHl4nECgYEA4qHmHJlA0Liu6z9Wg+/n6Z7+OnZAfTqvCUayPhD5lKu8WWC6LsI3
7m2AhkkREaVHWu+9Slte4c5A3stH4eEkSKSWSef5axdlYZc2ST3UNOFAzMkPle2A
kZAYWZ7XkBzptJhztgBiQUBJLrQ1SuXayvnrpgqIIYkeuKuRYc89zWsCgYEA0dRP
rMdz3+rHlGmNWgU038G57qGlWFr6NLEqSITYz/7Xp19hP/bfuD44PvniH9N8x/3a
IlgNqaZLU5IyFzIfYE6yuPsUXC0nNzxcc9FCiLedH7d+247jDOcbbQXOi3pTa8Ar
rkwHTzAbQXT8VuAOcs+cjDMa6rW9IsvHvuD4r9kCgYAqDOAlbkoYcCwEejwTPvBI
6LdDIa3Vjo3rqrJn0b59V2AbNVdWVbMLCkZOpEAGhiQ3O0RkB5ATVbGzpQQxZRTW
ZbN9Aw3EURL+iJAKBu7Y4PKlDKlXqDmyyIm8FzzoAHVcjOzrWCbi9Iqfn9BDlWKD
RtvycwHPNyH8IdlXzJwrAQKBgHirKVrKpSe7hCUkgoangd3AMiY6zbS/NS7CR/fG
dk0/WFPHtUyss8Hn/j6xQ8pbvGHi6eRgURMkMCOSar4ONB8VgxCATBgqW2gXjW+J
g0LOnUyVIR4w0QAllA8hjMOHiJvpuvUUgguXNcVx+oAXgBekr3mtFiiudWOiX2+1
Py8ZAoGBAKPAc1n0UbvdNjQHllxm9Ehok3hcVvJZRRBtcXytKWwl3FI6/I50/XAy
8PaI4gbysiPgMl+zTU9mIZGIxyMHNy6vr5/3g+ZceNadAsIQnJQLTMM95WP/nKcQ
XsAuSwTFviI2LBxC7Scnpc8JHugzP6a4oiRs8yqSfKXYGck8jaAf
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIURlqEdkPWX2ld1ZkYRM10UTM191wwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDKHNdtHZzYGVJlTaAmiJDMsNdVpyo3sHewUF23K2zMTUZh
2DBX1heO09RpOIoGIdsgm2P2T/+731O6Hi1+pJyLBq/7LtoPX5fZL/AT1uQN5yDF
xBUvmaFmnapEyRC2tg6H/YNBCTrHO3OKWzF5Zn5dZDmS8D5FcnhPups13k6YYklZ
ZewRTTUxUlnorKdDh2Ur5UPHnpxfG+yRYow/prs6sfQNj1Hdv4nsjEwTPwJQVIC7
xViZMiSWUaYMx0giJe1wggkuVYTBQ6tYCOtbO/FKErYS+NrZ5lUfUzmpzlXIM1bn
Ux+4SwMYddcbedVywMap7mzupD8ZQNCuio9Z7nc1AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBghZflsoqx/js1oQC2JfNc
gD5HWNqlS6JbupJr2zt7KaKFVQfXmMEUNcVsEr9PXIGA3vqDnpT3L7Ybk0R9knYP
yGb1c5uRFn5A7moAcJjgwUrDE9GQBx59KRXmK4DofcwinUPEe6BU8sn9VfqjTprQ
WFFLyt941YCxaCCGPgZTyGbHWK2pTQY0aBSQAyNppk+dsca6l2HkelkmUrS6I30p
r4nhJq+eXmehrtn8+zXT6qxmr/vw+F7cwnYyxLswBMc8ijcmvBbkcSEcFbdP8TMN
A4FFYyh0rIijlKTsoEyvUP7LGBBJv0d3RU30jHPBm4faJ1wWXLm6p3hQEJmLzM0i
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyhzXbR2c2BlSZU2gJoiQzLDXVacqN7B3sFBdtytszE1GYdgw
V9YXjtPUaTiKBiHbIJtj9k//u99Tuh4tfqSciwav+y7aD1+X2S/wE9bkDecgxcQV
L5mhZp2qRMkQtrYOh/2DQQk6xztzilsxeWZ+XWQ5kvA+RXJ4T7qbNd5OmGJJWWXs
EU01MVJZ6KynQ4dlK+VDx56cXxvskWKMP6a7OrH0DY9R3b+J7IxMEz8CUFSAu8VY
mTIkllGmDMdIIiXtcIIJLlWEwUOrWAjrWzvxShK2Evja2eZVH1M5qc5VyDNW51Mf
uEsDGHXXG3nVcsDGqe5s7qQ/GUDQroqPWe53NQIDAQABAoIBAHiLmzFJaDK7Z5lk
IxDYgwSStNwxR8zPQ5O1Wy/Uhp+Tt1bESpEY8BQP47CeODRQHRHlnElcjXrQSG/J
b/kI1RVWd7+owgZJTZgML3Slxn9ESxepS7mIN+usPdGo2n8fNquFWLOBfb02iEMN
AQUXTGcHUA+DmqBxFbD363rFjLr1VM0+N1vjw20auYGpvWOFWbhXjgWGBHuJhRNn
tgkXSsrOsPzbGIWw3GEt/Tlw50ehVNTSGA1jdxUlNHF7sGfFLVYjcO5AjCx7661v
w+w1eBwWI+SrYxXp1YgHlaJS1/u0vCvQ0kLcc2Ry+zpmesvi4aKVodKXWn7ZEsKb
qv+pYgECgYEA5pchaX88w6FiH80fzF+mcCcDnliw83kRtIWRE0XmhIL5ocnWuOcb
pgSFr5kEw80pPDt+IYrKHxyh/fVZV33n8JJ2fjNsHFwpZykIDhO2H2CmkXm+fTxu
gD5HIGzPx9qxvni8xjjXfSFCGvKuwGa975XGL45P0LsT90iAumkNnAkCgYEA4GJd
oRpSdxxDYuTvDHkvdlgTYSFAy/4njk7MsfnEsbn2l/p/xDx5H2nKrql/7J26pHKc
ODZcQXaRGaOi83K+vYAmHPC8zdmuEgh4hlSqJ04IEcU+gadxeCDh/RcBUPMvtBe8
nDl15HrGi/k1MxsdrrL4Un1mrvtwvfjbvX+tZM0CgYEAhS9TeBiqox/qig2zSRsS
CgMuvt3hTq9l/4uKEMS18WGpB76JzACIYqqIALV0IBe2snh2UK9WMQQbuJBmivdI
6RXfZOMUlYjRzSjQ4ziVX6g2bR4RXUpzVJUkBeFzXa6+LRKVjjQ0mqyD/wae0rhF
CkXK05ryFNCJJrH00DZvSukCgYEA2n0N3Jxr5k2gFEEFwGiUXbEflbmyhbBCRiDW
0wp5i/Gfe5dRJ/0WmA8EbBTiWr2viweKtHXCWYAhhAzB1DpMHuwUsKN9xRgMlsSm
z27LjKA/3UXqOoeYRrgGNdJb1r4mGj/uyVRuRn+Cq7OLKOtjeMQOZwxymzp9Ko6T
Ma+MYJUCgYBeY597VeXh9vwMlfgjIz0vbGjrIgGSS0YqM//SgfziHDv9Bh/sQY/J
zy18xbkjdbCulGGyro7zNDXmOcf5CUsgei2cc/vgESQEZpoMSnVvG1MWQ30xq32M
g4FlmGzdEiQiRxA8+9lzOPJRcQdUgS+Le7fOWH85q2aXrv7wp6lT0w==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIULNQ5Bq+zPWOGPtKDkjFf9aHtCBYwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDmIHrbtqy5/pMJq5NZmVRFbX8wHSciOLyUwWY6K6BgOtZH
8WaKoOS03X8KVnWKqXGcUY9DKWar8iQ+VbGP7YLw9wJjr4hNsW1DqN7uzxla3XIF
upT/tKAhZpiqOHKstGEoKwjVD3Dym5xmSP6ERQTfMolo7WaakTpANCGKW0tKM2Rs
6pSaHV4GIvbHSer/apt1zr2IBFQI7Sj9KSXZ1OhOZERSE4FigTAJvW5PEcuVsjwR
LB11vpPKiF7YkLmsj0MQRHlFqZukrSdlvR9ZLaAREJLgk7SwCwUSYGQEGhjiEkH6
vWXT/35IYCkiYNI/vcdCQlN4xBOOAXgO3c1HtikFAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQByHJaF2w67743OsMwKbQ5j
oWAt+rqivYmqJ6tVKEpCAZu3aMPdchcoZdfWRfh/tRP0SwkNE7PwIyRxo0qynrPO
gXhGR17ezrgz3a5AzQ42EXg0xb75QzpkXdrOZK9ynjer4jlMx+a+IJniYlSpyCxc
AnEKvnH22S4j1xCYC9zMDUF6Jqm51h+Pnrz2sHr7NyRu7Lq9cJ62rfyT9kFW/aZX
1/xAwzw2GmyYRpw7ZEiRN9Ipkjs8Nn6yCWOvs/wa6el06mXB/i/IvOdMI7/B3PJS
sOvOjmtIS04kyR2ZB4Qhkty5WSHrF0Se/9WH28L6a6bjFKLRMKLTRLdeZ3ybEOFN
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5iB627asuf6TCauTWZlURW1/MB0nIji8lMFmOiugYDrWR/Fm
iqDktN1/ClZ1iqlxnFGPQylmq/IkPlWxj+2C8PcCY6+ITbFtQ6je7s8ZWt1yBbqU
/7SgIWaYqjhyrLRhKCsI1Q9w8pucZkj+hEUE3zKJaO1mmpE6QDQhiltLSjNkbOqU
mh1eBiL2x0nq/2qbdc69iARUCO0o/Skl2dToTmREUhOBYoEwCb1uTxHLlbI8ESwd
db6Tyohe2JC5rI9DEER5RambpK0nZb0fWS2gERCS4JO0sAsFEmBkBBoY4hJB+r1l
0/9+SGApImDSP73HQkJTeMQTjgF4Dt3NR7YpBQIDAQABAoIBAQCTXdlPOfwCX3Pp
jWYeyoGctDHurbyRvaOF3xOHzMg213bBO2VfAQl0iSMBi7xZv4hxggksCScmlTmA
cX/zmzVu+b8d9xpiJmzCFzIr25NxDL4nzQP9e73PpdO9rchBsIFHJ8fQKMM7mUre
dYAHU+t6wvIbr2s1MCsNUlToNO5R5MBRrJjxqvDteLMrcH9Q6ae6f4sWscqs/oyy
yXa7Qve74dGh84PfNCDeXljQjXRE0080OMWBfY2F5Oy86Vf42q31M563ufKIcCBM
lMLKBZjc5L2AqFZKOERITBfax4GAoV3xfiRfClgAOA6cuQ385tp18LxG0IYf8Qcj
xQuhvyoBAoGBAPbmLyianEJV3j7gojm6dl5rcYblzqU6rDrCOGNSRh0N1bGBP/T7
OEe9bi7apK/09JN4sm0c4LhhyJDanCfaRQ9DRn0OKU0plELSWGvJ3XIAiCoeZSg2
I40A0CSg5SDnsFYIBdBqFi6E3oLwM3VsntQz3WH9O81k8KWraFdgMgipAoGBAO6c
Bv7k1hmvbc2j4CLdcf1hkpDGuv5bCBG/cPIg7EZUmpfeKnkP+7TyOzJJJufKE4U4
GOjkN9k9sYoNb7VubkWpdO74ylIszqo7bTI/6iwY8N+ZpJmi53poU3Fp2PTOJy0g
UcDDtaOiOaD+gEF1+5LxC+uUonL0g6bUmS9lpQr9AoGALGL5e21ARlS1ncw4nfQ9
r3/VaxEJc37206FzDbgOzs5b6ot3+gzn803E7ztzfAanqZN7UE5uv/ckXZZPmIKP
A81ucLEJD8w30UOLjeU+oG4kDJ5mRTJmdcT9pngeeSnt86mBkhRgZICSmCuitKuQ
akngtOsXwzcwZDhKi9rJY/ECgYAoC6mk59UC9I1SIPnCADZcVx7ZC3FgtPhyuhWD
nYDqANL9P/0S2lrdMHY850gPSLvj9NlBZOP2osMEL2MbKRB6wojsfna+OeTpbxXR
hCaSBhGPBWM5obyFr7KpayFNXLf4e98cofv/HX/chDoUQm/ZZnkgrY5iCqV5v16C
NOXxJQKBgEHFazeFqKKFnIc7oWhZUKvU+UQ04KKGFIuRg0IKhIjxySQGqiJQIvJA
DfNrpsARfWpfCo+dSVxBIcSUATKvA3LMVPaaYAZSj8n7YFA8M/2oCegtM68QM5DZ
Rc8M9EbKkv9/LE48h4gc9ywIw1PD14SGq30il8wldWRSYyry7/9t
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUTnXTzqEOILFs1Y6LuvX7UkxgI1EwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDWr7824CNwPS2WHAlYs2QpHVtj+nMn/nl02e3JIX9utKfz
2sVXy9dT0sW7VcDaeUYBi6pDZz8DecwGjvnBMAfh+bkEx9gCs1tY8Iqitgmekoy7
e7+zHJ1zuo0J+p/zeW+Lwg6D0FztarME2gm2tuw1c5FTIfWWnwotYetXxUWCeKNc
+TgeK8WnfUjRcULzyFRAA16n6AmqihfcfVmT/Jyr2eubKeyCJFGUx6jIClb+OFUU
0h4VCZzhHOx/R/X6B9HWJTWgdoKUxQcMt1sdlNuntOkgg1JsJPVPM/+NnijCdHEC
Wsk6MGCiVVH/vtR6ek3sDitsJfk36m5NjiDzeK9dAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCj7q/5jVqInWNHENfekLWU
u9N+cSMhDMyq/ANc/wm3OcOAYUODAmfgZDuGAmHW73BSeoEuXQdsnxQTCM0bVF5v
9hKcQkLY9v0tez7xcDwicFQfg/SzjCehbeKtKZGnrANLg1tEm2QFUuqmepbhatF1
NREBmX1EtUrZ8l9e0i1oDk13eOJvdkZ5pfQC7UOK2N7dAHQmsWJtJgHpGu9KgdDV
eKRf55N0tiDKFjumdFucvMQVaOtuZX+4bKrLuDE3y6lG/Bzt+ZHZkbCsYAqCtubp
PfGozr3jW+plZvnRz4X2GxQRWFw2jVBcBzu8f8Ahp7q62nT9bEfJ6fsKqwhX/KSx
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1q+/NuAjcD0tlhwJWLNkKR1bY/pzJ/55dNntySF/brSn89rF
V8vXU9LFu1XA2nlGAYuqQ2c/A3nMBo75wTAH4fm5BMfYArNbWPCKorYJnpKMu3u/
sxydc7qNCfqf83lvi8IOg9Bc7WqzBNoJtrbsNXORUyH1lp8KLWHrV8VFgnijXPk4
HivFp31I0XFC88hUQANep+gJqooX3H1Zk/ycq9nrmynsgiRRlMeoyApW/jhVFNIe
FQmc4Rzsf0f1+gfR1iU1oHaClMUHDLdbHZTbp7TpIINSbCT1TzP/jZ4ownRxAlrJ
OjBgolVR/77UenpN7A4rbCX5N+puTY4g83ivXQIDAQABAoIBAEOfWgiL8z2wV4KX
1C3XW65Dq/zC77DiTBmNZ4PaBEy3pMt/1ndAItQpaNUIPtXSK0XjWz8d71BF9gj+
0haS7Xi1cxzZYeX/3r8WDWURF9iV6rRHV2uwkLvaQACrq+RCFOudtXq5j/vMhxT5
JOQjnCV+AIGCCdxmvgrrc/jSj4F3sFiIpMh5z7oufTmT3vmcx8dk4dSCujpMywHm
+xFj7OQm3DGVY5sqF/tevkD2OTal0pWHj+EfvDaNWVWa9buCsjy8h7urPplLX+pd
ie+BIS1sID5YTRmFQrxzzbrDuE7lXB7yV47f0sj/+23S9yVqIpUIEqLhIFnrP2rG
iVFbISECgYEA+3AoJOcKXvWZYOHP4OeF63Qu0yUq780sk1I8DUSto0idoJPJZG33
RB1/11is+DvfQDt8/C5SpfNONvRLfDs3uKyJ8aCps4dyf4Mp97nTpibRkXfUSc6T
1cR6HWw9d6Om1bqDAgp1HceWM0pGRg57tPmLzFxO91Qh65Ttp0p2w1kCgYEA2pTk
QYUzoOgbJhQAkYnzGSP4caYst0lUq/rfFIYvL6eejoLcqowst0iX0tPfD429wJcV
P45/JGN2yQz8QrPbctflsUCPVQ3E521oem5FLNcsKr97oxzy1HF1PWjHX6xhZ6/7
tfVXaP2cCAeAKKCVvph3vDI7SzfU8ek0DK3NH6UCgYEA5KUdHFGtMKUOEPfHXbGs
KmzAl+lYnjBptJ43Val6bN1/2aIKpXUKQbrBokZVJHbtkS+HfJtzNM2H9pk4e4Qu
K5Va64s6RrOI/0N7SnaFbLYoJKxfM67S6LV+hnsDemQrNngg4h44WhhBEesc9F//
RpcW9YOLm4W6QsxvQI2KaiECgYA33Kd9Kzqnm8occC45A8VyHmRHP03cRcxy63mJ
uEVk63S1PTKCD7L54H6Urfsq8XGWP8Z5aMSLmzPna/8oWOjzr8OPCk3XUd6Jusdh
yr65GAC8qBVD+YkBzEFHQXj6tYZrRmmQ9jOxrGbtEmWpfGjovfSTz06iCZHNhWj8
+Ioc1QKBgQDTA8/Hw9zpG80MY5e51AHF9amNOYGa7/OkhDBAs+U0zjQcF1O0IlMK
eooQuhSf6RX0/DI2JgSs4Yf9Gx3jvCGW4w4LGTN3veiyQeLocqbNlGijaz+R6bcP
zOfGG0s1vdq/thQbnBerx9sjoyE9RIeOmf2c7Sv3vn+uQDTR7QIpVA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUR24x4LgpE1t6Nmpk9Lbcm2p9bZ8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC2ye4u+jn4ldMnKFJTrpndM/mgaOI9irWCQ9/kES44RvYz
SCWgNIqU83XC7siCkDTAfmQ5dPDgwExGp9mqbBjLa3QuWLiBSmstk/RdvWyYTyv7
Tk3BXjmYU6nbBr0p310+D5Jw8RKB7O88wM603E5Cb48GKmh71DY5+JxwaIJbFATs
DmPXQ5tIO+z2WZmzB/Zba7pYOILk1XDR4YPLgVdvOGlaMCkfMALYKtdW9ek6hIFS
oPlm/mbzbIld80PYP9E3Sf9iX55GVytuIt5B0u6PbUYFcrKyNld9K1UEA9fyNECa
KUVe6UK1Kc+LYGdkRv/qAmMG85zMM4CHs1dP2jRFAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAREhwgP+CXusazRom0cMeb
KfKZIY2TMHWTYceAB21vUDSor8dfDNZNaJGqNDWJiwxMdqCa6k5u4ClBts2silfs
qYWGQvUpygD9dq9Nazsf8GATZJ/X5OfVKSb/j9OsmikirngsB3KfoOVUz77aALec
yuH9tji46NtYUXEMYsCvQ+8SAmLQNra/jqzM/SHAL1Rz2JNxXY2ldBpsWuwaau8n
j4FqvQtT97zC/RV32B/Io4/LJnD2bvPd41Wf5YutTOJXUFuVDQPD9rI0VkZk87a3
o7oGLlusWLZ1ZIqTylCNVtv/Lz0JXwImhYIsDcNswVhNIWiKHSJkR4aS3gqVt4Sr
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAtsnuLvo5+JXTJyhSU66Z3TP5oGjiPYq1gkPf5BEuOEb2M0gl
oDSKlPN1wu7IgpA0wH5kOXTw4MBMRqfZqmwYy2t0Lli4gUprLZP0Xb1smE8r+05N
wV45mFOp2wa9Kd9dPg+ScPESgezvPMDOtNxOQm+PBipoe9Q2OficcGiCWxQE7A5j
10ObSDvs9lmZswf2W2u6WDiC5NVw0eGDy4FXbzhpWjApHzAC2CrXVvXpOoSBUqD5
Zv5m82yJXfND2D/RN0n/Yl+eRlcrbiLeQdLuj21GBXKysjZXfStVBAPX8jRAmilF
XulCtSnPi2BnZEb/6gJjBvOczDOAh7NXT9o0RQIDAQABAoIBAHu/0BpL3A142aBs
AviWf6KrenfoKisCCopri1trakA9gpcLZDXG/H+FKBfV8ze5i406xH3FtwJiDgHT
x2BCmLK3R8vM0vTtPgx4W3tPMAMZrqwPwkKEmTeQhLE9Kbn8d7L5deoyu5Xso7cc
zZTShcUio9DHyz7yV9f9gWP0zTP8/qYIlWTS6laSsBKlcemsMmSklopj+aR0Sbkl
8qF2rlywc4994+ZmD/TEQMSJ/BhPfUkQqCQdoOj2tPIOPtXFqckvZkfvYC4pWJLl
61GXxv18+y+QB5uMOUcTQ7vvLVPwbfXd7TS1bhUiOFSJw/fxmMtOOoGDOirxnfLD
8vBeVUECgYEA7BVUmT35dGp4tEvvvl/RUJtmBdj0prgMOjadO5DX0ZbqNYWFakuw
p9X456G1T3lgRqRp5YddJpCFSYH8YnKoOSCzZ80jIUbjDW/0mnESZCb5e8TXyj2d
TxqZpOrVkuE+Dadn2O/iEROz/oBXN/QpG58GqptsDuSJ+P3OjVW1TnUCgYEAxjWa
V/NcMWqY61TJabAy5wlGlF78YjdhNjS0a1vq4NgQcO7k0+Jd0ErLkMpTN1B1t+Yw
MW2BMz1E58AFKUzHd/f6eeJGzFjEV4cirwViNPkf0X7/mIGAAR/6DZLay/IxW3fC
8kWe0cqKFsXAa2TAtgr0q7ji/XaBmmRihqo1NJECgYEA2d3VdJX837JiMgDh/o3u
XLUMMdlF7ZVrs00zTQUeJg1floTh2nZ/UGPmj9xrtiwM7SRNlcSV8kDswCl1AGVP
WWkUJ3boNI12e7AVy3ENx98v3UiK29iAk7+4irks35995JvY+hpmRdwo/3TxCHIK
fbMEM+26iwPdUCrpswSljQECgYBZMf4G3ij6w/GU1U7eFMCTX4U3d5czy6AfeJBI
T9De5dxgNeEbyJ5XAZGh0qqoFbkjzJ6bX5/oowXDFJI+B6MrxZgeCUm646dXjCR7
hnyvQfyjlfcHdh9YYj9wpEl5xb+YXciIpfPWjMKfhNYWffyK71sze7wKO64PAGWm
HCpdQQKBgQCftgQ1tpeLhjiA3PCkYUpj0XnErP0+FWhLq0pEkwsVKfprxoMO/foY
Ku3/XVtRat0w6/CdQpmN+pk9PDFle/rnD9emxqkeo8pkDxIo7bYSr5wF4oV9c36j
TTp/SFMfM0rMkuoMeNM2uVXroCXOExSbMmBcWfthFwoCJv8tOCGLhw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQsRmXdBM+Yt81O+qtGzJpULDwhcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDc2huslrMBGoEROWCsfrd4LwHPSXrehqP8uthUzpsxhxJP
HU2bDi4Q56IiAaXl33txbDnKE7zOE205rp0h/k3mvnbo9zBFHZakIZuySP5L/+ry
+Jyld9QuggpD5mWWHW6lCmUtGfY0UJJJbr6KPyMqzzQ0xrjLAPWqVvNR19Iapd5D
GsWgBSpKyUIwPUf8JpkFvSv4udZlrONoMA+/PAVEeCgOKbWdwi8vrpR43VcUPSe0
TbxE/bWHgOSDW1FtE46logzJLOzvx/k3Lhvumfrr+znNsZyjk14peqkdAUtOA0dm
VEhs/wHthVkw/47MO7G96DzB0NI0++anRhNXLiAZAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAVNEaquHBV5LaHJDGrr66p
xPuM9sjaahXr01VfAFBqFGzr+8ZH2T7VL0bg0vO3aimM+Kp45eRGM+gffZ70ab0q
94CVT++3rhoro6nXhx1U1lHRNRqVOyGImwMbz/MtmIAeme7My+kZDcNlFg+MC5DY
0pjN/EAoBslrhGp7yWzEh6oo6cKsYajfqcrewwMRrY7shqrpH/fs9gAB4uzryCVV
54tBj69C9JVi0d06YijpLcUT5czScd6yPlX61XKR9lpKUDyEGbRU+4f4DP2oJzzq
6tsME2HXXcZr2fsxkBeCjZpDEsKPMxsHBnebwSTNESCLQgdQc7wJ8QVzgOkAGoNg
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA3NobrJazARqBETlgrH63eC8Bz0l63oaj/LrYVM6bMYcSTx1N
mw4uEOeiIgGl5d97cWw5yhO8zhNtOa6dIf5N5r526PcwRR2WpCGbskj+S//q8vic
pXfULoIKQ+Zllh1upQplLRn2NFCSSW6+ij8jKs80NMa4ywD1qlbzUdfSGqXeQxrF
oAUqSslCMD1H/CaZBb0r+LnWZazjaDAPvzwFRHgoDim1ncIvL66UeN1XFD0ntE28
RP21h4Dkg1tRbROOpaIMySzs78f5Ny4b7pn66/s5zbGco5NeKXqpHQFLTgNHZlRI
bP8B7YVZMP+OzDuxveg8wdDSNPvmp0YTVy4gGQIDAQABAoIBAEYIa+oox468Bt2d
YkiQzkEwNtSyqmHSNEI6Rctu0Mu911J7KlbXAkieC03ZU/A3E//9n72y0JZQlrxJ
4M4cxDs9fpuVdxsTrOdTOPoqJ2mWN7zglVvrSb+NwQ+TCfe2UZXIXBkXOHmSazEa
CxXvu4kht55cvdCx9zUS6Ym0dI26IGBybmr7zwOnCg7Kz4WTfO2JB265mLu/B6wV
V+W5cLPeh8bDKl0Za4+v4XXdzMmUliBmyGyyhT+VcuqQWwFwp2OrsPKAth73S4rN
pxMd1DrOyrZtAMgkdfzkNTJy7oFW54ns6OxG9p/p/t5N19HCL/kpUGcBoGUQFhXb
YxrLy/kCgYEA+xQRNVJTQIqoK0tCEv5dIyziD0ZfzsDDhc5+qFV+7uKsfdyRhLGR
GBP9JfQ7Yc0U1W2omreUGRSwVxU6YpqMQQS7tEQQhiQp3yHuP45mVKG20qqFzMDG
zeACkTOSIyh0BMkaN+nxkS4PnqlRaqUsyuBRsomof6y87g86cELreYMCgYEA4S5c
uf76WFOg6IFwM+1d0P2EDwa+jeXOvZI9fQ44rzyUNkMZfsvFw7+h8hsZHihrKhTR
hCemvEcgDIfiCmsCYMRpoI4oJUQGPCeD4mCu8I/ackIX/UCsm7OmoYyNX9KEPJ4C
eUCocYaETc31wjOyXqHzjIGynZd9fCFHRUjyeTMCgYEAoveRe9SlqNzW7tL4Xi+v
8GbvjA6XnTFNN4qid0yXCSMj5sXFxiUjEkfXJk1yRbbBcQ6uQ04o2GavVra2oM3D
f2g9FXKgbxEGBIiXhbU+Amy8p9x64D24TGS8Bdc9YYieVYTaebRlUWBeTxODfv8b
JcuX+5SSQ9yw/KvxuHAXO1UCgYEAjhG2JxMb14ZLyuV/aQOlYSnRm7lhmB0ZZrlR
WgkS8lyCFgoXl8vwpiPNhPZbzo8prY8c8QgjRj6Jld5VWsVQ5sSE7+tAoOJeHK3B
o53kQZpA9D2G7R1UyZd61gnbWE11aNk4LlAA9j8sUfpTx4beTp5XDpr1mj/tx9cn
JCt178kCgYEAttYPBKitz4UVAVfFNdJk68N/Tuw3KoZH06l0TCy1Ygof0S2GZpE9
iWNVNino9Jw+AjQWK0FgKUVurK6fiBTlvtZHZk72nJRTGpeIGwa2kZbeL3qn9nQm
bsUE07d0gn+0Ztdo5iI8hB+y3xTN1tq4hIa6xCXKHz5Dnytqkon2h/Q=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUXa72z76zyiyFs6cTa7GIU/m41T0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDTSy0YIggCwTF96eLR2AxXmpXg30F1eG4SZzr6xWd5sXiL
crUjSc6V9YZRPF+g6ODEryNYjSxWlYf0EtFPD1MGLW+7ssUJrWK1BX+FFCLvjQX6
ShfRFoOqmkAhWp813xYaWihdLLv2UglphfekREFhRw5h8ikfk5JA3AgTFVGFjB/q
1pZ7gWVamhjjzvrbhiXdqcHDqMuNUMQoCuPLlMOq1D59nzYhUUYZOTP8aAOD2dj8
a8plM6OQwAuQarqt9DW69Tm7AxKbFrXnzXqTT4Ccp4rEJxscV8OIP2DVioFLV37B
EWq3pVcarIJku+Lxcpf4C7jXvhBUYAFVeQLMmjzXAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCSc1CA9sp1CEbEV+7+8EOc
5v3DU1rTEW4dG94MiWDXH/s8B+nWb2lsXLd9Gmau8S+/c3c8rW3eejS7YZ5w7lnb
NOdc8SUwPDM+/f89UCiEeuk9fUIe9EK3pER60Fn4H/0ZXQhVob+1lGScnIyx5vr0
Hq5rPO99qnZ3kgLeYRfHQygSpFQ28XHOkQGVSklgCbCBdE0lNWKpaw8oxw+Ki2zb
tSGF5Uoel75Y3e2ZqtonZCuvE9Q02LGmDmmfSrRuS9jW2hvV/CHpRnv02GMPQT4+
JTKtqOeY6+hI/eg4UKBYbGLY2Sn1irKMRFwAzftgB2eeU+Bhxb4ioksFlhDvzkMf
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA00stGCIIAsExfeni0dgMV5qV4N9BdXhuEmc6+sVnebF4i3K1
I0nOlfWGUTxfoOjgxK8jWI0sVpWH9BLRTw9TBi1vu7LFCa1itQV/hRQi740F+koX
0RaDqppAIVqfNd8WGlooXSy79lIJaYX3pERBYUcOYfIpH5OSQNwIExVRhYwf6taW
e4FlWpoY487624Yl3anBw6jLjVDEKArjy5TDqtQ+fZ82IVFGGTkz/GgDg9nY/GvK
ZTOjkMALkGq6rfQ1uvU5uwMSmxa15816k0+AnKeKxCcbHFfDiD9g1YqBS1d+wRFq
t6VXGqyCZLvi8XKX+Au4174QVGABVXkCzJo81wIDAQABAoIBAQCK0TwqO8mJjcXn
VK9JcKkDMTPBDsyh0eJ3Qs00DleiUx/AdjddnNMWIL4DRygIvpdVgT82oWF87Tbp
+yb6yzWfvGBJL/VWG0zbY2ZZV1ZwjfVccCtfmmwcvMTfZPtu2EdcPtmABbDj7xfx
9SszCAjwUU+4t/GepkSTSjwf1YS+uJRm8JmEVJdysRo2p34hps0UQEQSQNpSEPsA
lG3aYtR0spLQUXXoDGBxJ/mHFjV8mlmYm9bVhfAdjLSaaY4z+e60LgiTUVApyLuO
Mm8OP86aIxK7Vy4U+okg0ZlzL3xgsXiReCfLDR4BaTbXYS80wsIg/tqB1soLzzSO
qGsMXMIxAoGBAOxnudUSXgv+bboPdA8cxfvZfJNc23/uBXLCtnEMHQCYok0jGro8
o/Lsl9HkPRyX0DQXCaOwO3CkEXx2i3J8NKjTJuyLvfVefqclpGSxewq8+N09Ins9
wxOow/3nJcDPJrbdgZP48cIqFleNbmF/CmsPFf5HWb6j5tTFhFWcwR8/AoGBAOTO
nBDqb8HjWXBOGufitEG1kUwjbsZQ9wnfbqdlugni1QurY1X7JlbAG9QyOQmLXngK
6NQVqIkvu0aWdiFavg3UUVaTnVmgKmmmO+npCvJmHUvwkKQaDpbScF4d1wLfaWe8
pkaoaXUjuTQMF/lPh7xBDNMPz3cvSqjO+TDjrJRpAoGBAN/rr/2+lA5QRKbEFG5s
Fqvi6Ti7771ROx/khuK1UpNKABGIeryEy9ZBe9x3j9sRgUiVua+uMd8TyOxXbOZX
95khx/CuvJM5mkXAReKKqb0WGbOVQJ/zdF+er2ZEF2J11HnJff8nAfej3d24PSFk
L/4QIAjmlH8ayH4pSJu/Cr4JAoGAB7ZTGlrck3t3S0rGq2Q/0Ssuj5NuK28VNJb8
YtYR9D1aEv+e5IoHm8rz5S4gMAsrjv5HJMbqHF2ogVOW/b7SQyMR7sog9qFobJE2
2caKIOuCN0oPhgh+z2Sedv2ofqdLJTz9mcoZa+JdXry9niCpIZZLuV2CD7FfYdtA
GP7DlWkCgYEAllfMeW5fWwJsio/N8PDQRISlN8yh5HA9DPfl343c8cGCx5ENl9n7
QOqa6xCTtTWPdDwnTQ8oCf5v/97bGPwpWrYxFxqzld+BIc8UHdtBEMwqzptvw2TD
i90QCyFVv/7y+izXLsrTUimCAM++muTYyXhfq6Z+trMr0PzAz5yxNmM=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUfuygNa26jw3yA1o8IQkLYCW31D8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDlsfb6//PmK5sQ+v3l3+IIjiTdRcoIxHB3e+fMu6kZPD0r
xLiIbQtw06CZsX4yVF3DaiIPobGKfI1fv7pxyHM5OldOAn52SFIWjnU5PNGfrw7H
+6Z1yCnB6lC89UO39ArbfiNrYGpf0Lq99ECHd/EjRP/mMd717fOQ//2zkhzeenXC
9jRffLZhkhblPCyFepVBAmBQPKB0rNmnhblwtueUM86LWPq0FrDp0MfP/HbgPQ/v
VxY1Pd0mBQ23xXnKCQDg4buXAqv9IVd/kNxzG7H8+5k2Ji1QSoSi301XWWa66kXu
svWc4125avodKiC5t3Czbce7kLAq8mvU32GacJ+fAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA5M3qJYfjlVzdXzu/JTmG0
4Mp2G8cjAXcSWEPwz+FI6gImLrA4tZz5MER5WxMQF9ALKKPt58qi3hk1b8Ko8OUa
wq802DBkg+LpurAmPNht3IZ8s4oTkSWOP3b0FYA+/rYqM4+EGBcso6cGSl6msayc
0eyUO+AlWYg+2Bw9AiDEiAiLMaODgmMh6ztmycNluMhP8TNOzQRqFlrEs6YvL/z6
tryToIqZVjIZogcU5Bko8KMcLOEWbLprSzSd4CIJEtuao3TdbU40TZmhUgcorX0h
GKaAgtGOxcYjApuavtzr3BA1X/HKLOUNOMDo/27lFPSL2PhSBBRZGGU56FQm2LB4
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5bH2+v/z5iubEPr95d/iCI4k3UXKCMRwd3vnzLupGTw9K8S4
iG0LcNOgmbF+MlRdw2oiD6GxinyNX7+6cchzOTpXTgJ+dkhSFo51OTzRn68Ox/um
dcgpwepQvPVDt/QK234ja2BqX9C6vfRAh3fxI0T/5jHe9e3zkP/9s5Ic3np1wvY0
X3y2YZIW5TwshXqVQQJgUDygdKzZp4W5cLbnlDPOi1j6tBaw6dDHz/x24D0P71cW
NT3dJgUNt8V5ygkA4OG7lwKr/SFXf5Dccxux/PuZNiYtUEqEot9NV1lmuupF7rL1
nONduWr6HSogubdws23Hu5CwKvJr1N9hmnCfnwIDAQABAoIBAGKeWDZIMoW+byOJ
P/20dC3MKdO/JRFCli8Wyd1DLUUicfkay0f32ZOlqSyT4mTliCRgqyMe/0VAWMql
XP2BXMdTXyylMXrDbks0+uuKS05OMQB38W5cdGFHo0ad32dZple6/qYZjVJ6IdNw
zUvcmXHVLDG/c8UPVyYIYvr4XuC9zwc8QyY6HS5FLL2YeuDWXMFqhzNHRPuLUebP
cFHxM/doBHuL/hOvRJiwuaG//od+f/j/2tAjpg9Aw0+H9Swyzjbf8SCh40B3oNHH
C5FfU+F1C5vY09oq1HCJnuNuYyKz1TxUHcm6FZQbbaFcqMYK9u7Ys++ZCm0N6RJo
JMSP7uECgYEA+UO5pmJGai89V2/OgghxCjJCHy2eZ88Cn3iz2G6DU/ispiSOig+r
i9LRmoI2s9ip0mNL8oVjXABHpbohyWTn6PNFZq74VNvfGFyH179nXPJZwNszLueg
Aky47Sjmfbr/EZwPsaSXWNJVx+c0o7AfJuvDOC3PDvRIvCooB+RCwckCgYEA6+be
kZG8Hd2ys/hRzbQ27YS0Rp0uqLWHda7HxRVUcIB4eYFVn/kb3Ll+WJslO9/FZL7w
e+IWrU0N09qsXLXGN/4Tn/W27kf40F1kIcHaUGmgEgdQ9fmcBQIMGxmHr1OX8J0o
CnjMaqvdHkwQgiBAVoAtZry/ci0IuRJCP465SicCgYBgMygaM8FzR6oH7cmoW7Os
uLrWJ5gD/lvHyiC2vegHZ2jScjdkxylwvDtSw0BzZoIcBWCRR7OSFTWRm2VgwYXT
XNgDCjIjJfxS/Zsbw+4TbCEBkleNma0iVhPky60xBxNb63wPFjOm/v5GOVASgG11
avYb32oTHmpX3Hk4mnq9KQKBgFrBNi0wsPuYeBCu3uHRjDQykpx8CiBTvipzNF3J
B/REKJUuQb/KuYJgRpBWF6wCOdG5d5FheLHxa/luLlN4hyqxb+FhSaBARiP7WfN2
vcOj7zYgZHBNOE3g7MFcQAwej9y8yVPGB3aeafIm907ok3fz1gOpZ8nIM4vnz17e
TMCPAoGBALrKGVHHstz8NNtCwgthyRrOsh6shgSQrQ545wi6FVyXT0AEM9mI0x6D
hoErSrwA3WAikT4homKcF8skuk8IEEureOBLN3mj8YsrG8Ga5fUmGqxSMzf/IBK8
pVPqryaTVINRh3Yk9EEZixme+u/YZ4D0owyCdph9yG6ojNqMr6oI
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUWOfPmS17sBQ2KK+z+yx4bCQgBiswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQD9vVqZL4co41Wj3v05i+zWg7J+9ODBraJDHeEaw3T7fXDD
I+ZmzNDER6uWmEGqFOvXHdwi2b0mDa6+LLOB2ksOiLknMME7rAF1BusxhYLypF7t
8uQXq1aGQ4fb8LN0llRR3EagfB9mQEJtLHksK50Q39tL+00L/Te56zvjwJR4IwME
MifXGQF0TbN5ofVPOxVczpo5cULvVyLst8S7C4qCs9iHxWFe+o7CXlJRtedNL00+
SdqkTllHXeEYM3nmSoj15telQDTW9AJyHQUTB34qEt8o2Oa6nrrEBRNHZGlBmwcF
EJt0EPpp6A4lHd8Iq/aQAhrweud/kWzde9oMBx11AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB0VYSPGkkpREqo5NXcXn3h
vhVmZwV+M1ZZac0/P5g/ILxhRSIWn1JTLd0y6eFznEPOYrQHZws33jsfZlU4OyT2
8Ypxp6v2TRZjY4RpEPy85VAqu5JU0+FZpJkHt4PXaLSnOX3Nd1XZi0AXtQHLvrTK
qEe0A4v0hkwAQK1Ds02udRn2eyHSZVfMVchMPJSD2wrlZ5Mz7uIWNu1jdTrNzHsY
sSBZlwrOzUYSgYP9YucbzEquj/tmn2rhZXNDaFZZ4/Rw1kcKH96vBTIxKnf/ocla
bYmP7j1r3Auw6AxLR5zUtybAj2M9tdE1c+qSP5mvN/ckCBhwOP1XuGjHs40bAiea
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA/b1amS+HKONVo979OYvs1oOyfvTgwa2iQx3hGsN0+31wwyPm
ZszQxEerlphBqhTr1x3cItm9Jg2uviyzgdpLDoi5JzDBO6wBdQbrMYWC8qRe7fLk
F6tWhkOH2/CzdJZUUdxGoHwfZkBCbSx5LCudEN/bS/tNC/03ues748CUeCMDBDIn
1xkBdE2zeaH1TzsVXM6aOXFC71ci7LfEuwuKgrPYh8VhXvqOwl5SUbXnTS9NPkna
pE5ZR13hGDN55kqI9ebXpUA01vQCch0FEwd+KhLfKNjmup66xAUTR2RpQZsHBRCb
dBD6aegOJR3fCKv2kAIa8Hrnf5Fs3XvaDAcddQIDAQABAoIBAHmcMTnN76eHHVqG
2zKjf4VoZTo3vyjUQTqNrX+YQg7ulgbQw/JtI3mPKAvrOT18/XOCWilR1jfQwvle
j0IjD2oN2T+RPGuPCru97ycy6AnHAcBlczBs6/E5mHmvKTMtgYgiXK86DgqBrdSJ
RiIHXSXjREVsUgb2+6hdt7x2ZjIVEWTbepfJ+gA1y/4GHgrntC5CtDkm+uh3W9rM
HnI8fmnpTB7nT32IynVbQy4/+ZHflDYMoKLCIiamvyk4L/mSghYD2YFduoLlfAqG
r/G/lA5gzpnrzuPmudIil//yrEeEcir8xkeuCC6dYQU/T8AKJh/o9jEcwHA2SBVd
XK/UPgECgYEA/12P3hhGEST5j61iNQQtSr5p4vX12o3Ov2FSJYi/qzqDyz5GU1r5
EGYej4lBQvR+C98hR4bVjJp+nciOcAejtaa/Oz+UU8nyfS6Z2NXqV0REZyAEeGLo
dVvUIFM24j/mNI2B20kJvAvBAz8Jy9efbBphTA/38JxBGSLKj8VTGbUCgYEA/l7B
+xXACCPGeF3UCWBghjB4vsut+LXiyf39b1n7BCaHiWGoiVKF86yUlaJu8DGxMIDx
U5jP0hjSww8I3qBY2K8iAegyMlH5O3RspEGNL+mIRVFMditUKRHT2wUsf6MkF5os
GxKPAw+nFheUmLsdin3Z4B9TgDp7s01ejFUjTMECgYAd8NZhb+8nK3KnSejt1mOJ
E/JOThBZY68N+VcsV3BBn0a8mbydIVl6dr62jZ09QHVW5v576G85YRPfZBhvQjYL
olVhmP7HJDJuQvx+0/X57WMnxDVB+DbRK8cfUyJoPJ29I6pKD7I4fhhPTSDU6Z8j
iaRGysiDSY7IZ6/gU35+0QKBgBt12VUk1PVL/2oRHwngGKuD4hUe4eoeoJwTyl9S
BHI/QpSHMW2ZthJHSEcbIQTXKHzG/sZ6kbzppx8dqWR3RQAnb/FqwriB9vj/KZdV
6EsK2AY7r5h2NwC0Bv33AgXJc+UEZMyLZVr8Ppp48zbFxHul+HZki1wldCM4MAPQ
UR5BAoGBAO+FGYfEeYmTVo7deE2GstA990IbuJxYUbXapSDGZehlu6calWGSg+dd
l/hugFQ3HiUxps8veJIHP5W+2LSgsN5zBT53I0YRvfK7/juAqG8Y8bUcDU2nG8BQ
/v8mMVAlIqNeGoD3szW1/6BBnvHBi7bKrAEoZGcIiWzb89av7upM
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIURUSWnNQeBOShv/Sz9MuDq2t6VVwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDEDI/6MSomdp0AjdEuQgP6og1bMKOb/X0G9mEpvKjyIl+8
SSijACXVRhSG7Nx0tU61pebjXF2ax6jgqpzSrrlv/w6WxSmRcqbrdZFSUWMG5FFc
dYfSKyrMmF/p0o0kXQRaBSeIhkLnGS43Zna1w5b7ak76EttzQd5uiJ6bG7vCpGn0
hXNgdXtRIaruK4TWt740F2vyhIRtsEIUURaLe8MPT8ey4lm4Fz2URnUvfdMma7GS
rZIsT17kw7SQBlaqoGXslYNB2yMdnAWRJzuh6cvnxQax2Mfciwit5fkFQlnVPdZx
W/rLffyCCef9Z0m6WArb76OTwcCq4pmwh3dfOi/ZAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBu0wa4sLoqzpBt71pELonc
siZZ+dCLuFCXvyt8nQcN8arR7Dd5/eb+kn1AFNRFggbnf/z/jTc6ujISUrHIzAkz
mVbuwzyA3gKzZfyTgv6H8N6qvqLPBTWMgs82UXdKE4gXuheUT9+lAp6z81FbuFK9
PSX+gebb/WwxdEP0w7A4mws6udBnOpPW9i0ArZKNKgWl8RiaVxoJWt74AG/t6HIx
TV2iONXfZJO1k4rJb/jsmOavfXDYeEVrqXJ40f20Ex1wWPGd5Hm/yOrFutF7nvye
mHxa/DuK2vpqPuwcJLYr2FHatClZNiCza6JLeMq1CWgEJ0Io9fte87JuP4ZWi4Q+
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAxAyP+jEqJnadAI3RLkID+qINWzCjm/19BvZhKbyo8iJfvEko
owAl1UYUhuzcdLVOtaXm41xdmseo4Kqc0q65b/8OlsUpkXKm63WRUlFjBuRRXHWH
0isqzJhf6dKNJF0EWgUniIZC5xkuN2Z2tcOW+2pO+hLbc0Heboiemxu7wqRp9IVz
YHV7USGq7iuE1re+NBdr8oSEbbBCFFEWi3vDD0/HsuJZuBc9lEZ1L33TJmuxkq2S
LE9e5MO0kAZWqqBl7JWDQdsjHZwFkSc7oenL58UGsdjH3IsIreX5BUJZ1T3WcVv6
y338ggnn/WdJulgK2++jk8HAquKZsId3Xzov2QIDAQABAoIBAFHGz7PUGDntFjZp
8YxzGwfL2vhjxItH5IQn94WaXXqK3hZDCgFcCWv6DIvvd1HzYv6gUjwahi0PBaGZ
aUr0eQN/h81aNqmmAnyLEPAeZMk2Kb4AhIQlX3fyQ2fcXOWDK1KFfeUT5ApT1ZRk
WDYffPYodQMZJJLiMe83a7lViy93+1/6fT/Rr1taSnIZOp0qsYlwKoi5Yzi95mrI
X4sppl3QCRKUQ0sIOHb7L4jI25yLxP94yLM6f0F2cV41flBIz4y/oEi2MFVRqF1f
hI3//VpZEEqyqNsSKzUriJf99EdcFa/SpkI1Gn4SJwep1kYBcbJJ2/L5m1metMA4
IaKbYtUCgYEA+yYWnIkesYbWRreNp3WxcSm5y3kVXrf1ijCwXeKPNpEYLR+uCyaG
eoVihfAO7r39R+q4DVEC19uPO9AuQYhiRWgSkOTBxj2oDKQCo8DQDhzJLLC7drLR
a4ubYbpX/JwaTf3cnghGwTgGpxur2HMH1eGDm/zxSfTg5C3k4iljsRcCgYEAx9YC
nEWnkzG60pvjckghcTvB5NPcBUdw/UZB+gUNFfhpfXbOxvKf7Y2FkAwtU7PQD8gj
SqCgvSBR0mjIX4wDv+qj4bg4tw0XKHq/Ab3A4wOWwTfvca3swrhjuk+yFvn2OgYF
r/flx/jJmqJANt+AAbM+79eQt0JOef1XK84KXI8CgYEA9OAiU+ZugvHRo4n9GDZt
GMVyXq5k48HCK0dl72Sj9rRqOjUVYdHidTvw4F88cBPXDXQSmQlQGF//vHYzY7oy
9zGOSLCDL2OWoxyXZkrtkZUHogeAATBBePbaPeOPPsKF811+6qdvNZ4G/pDAcX9X
OHd193YdXdriHBmTfeCVT2kCgYEAnt6vOJnPvZ+9jQ5N5l8d5y3A2jDsLG49j725
WhGF87+H7izz+wqMxojKdFiZ+H9tm/5awEuvPmxhYEvZcMyZdowOObcBr9WCYbYk
ADhhDpmd0oKro87H+Y4qCsatKMMUU9DR2LHWRgKuFHeFYZqR48gi8v6HmInoZedY
1AR8DFUCgYEA1OGjovhcCK3UsqlN3tGVqS3fZieFBJM7JrQ7NJnsHw3NeUc3qmQo
trUJEr862rWLazcnbRvy/Z8WgwwVOEvbSFpmigTLRQMxhvw67NcCqwgh/A077r/+
9JL8ek8G8zw0L4PSjoChSwE4hM0QxhFkkwPxjUuBuLmd9XvwrHKJg+s=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUPwUT6RFj3c1lZddwvYGkWtbwHzIwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDPobMhkfO6/94LcS9llcyUkzxSeRcWOnmtEXgJxwe8biHW
5CWrNu5GMiCFSs6Z9os8M4Xl1s3DvYCfxiG5XaA7SqLX1183QMS/a4zOPbozuVL7
tyLpGx511o6gQrHMPFIqc50SVPeW2gMd/PW9WcYXI2rmMOGMfUhI5kGSZFXIWZzT
DRdIEyFYsMh0vNPuMGhcuWglXD1Wv6LGEoDsvFnmvqzbplxgZeSilvUyEMhxx/gJ
XwhsdXnxwVcdg7DWA1adELbiwx4TrA8ws+r5EOK3uvmemxMhwcjMtKPU3LvafBzK
R5MkMQpxY4RehqO5TiCAsJXMrkLoKkMGCtfW2TBNAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA466vxCP9fhomcXQolSuIj
speXwl0h7xPZvT+0dk+HVJbr/peTKMlg7szvwbNmjJHijwlHD5oim+GB6+WBiSXS
G9ceIe7bBLoPRizsw6b963u8jvKHPRXux8HNspYw18MV8E4SxMB6Sqtk+i8HWgcU
kSu6wjQurRjBMuZtu7abRn8gGhaRWMbu0TRrJlYRDpI6zQJfo+HWc4Wn8knJ0PGo
BqLKD7kCrTqp9eES6WUKMBJ/xLRdIK516I8gw4mQJxO//Hej0o98bkFihcSZMT0o
y4QKE9FN6TjHYPTllouTn4G8e43PnqYT4K8pium+tIuO61W+4OsgvRnk7ykFJpgj
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAz6GzIZHzuv/eC3EvZZXMlJM8UnkXFjp5rRF4CccHvG4h1uQl
qzbuRjIghUrOmfaLPDOF5dbNw72An8YhuV2gO0qi19dfN0DEv2uMzj26M7lS+7ci
6RseddaOoEKxzDxSKnOdElT3ltoDHfz1vVnGFyNq5jDhjH1ISOZBkmRVyFmc0w0X
SBMhWLDIdLzT7jBoXLloJVw9Vr+ixhKA7LxZ5r6s26ZcYGXkopb1MhDIccf4CV8I
bHV58cFXHYOw1gNWnRC24sMeE6wPMLPq+RDit7r5npsTIcHIzLSj1Ny72nwcykeT
JDEKcWOEXoajuU4ggLCVzK5C6CpDBgrX1tkwTQIDAQABAoIBAC/N6gFTqksmuAfo
YmJAMB8RGzVd3dvnULZxLDMMGRLgRHhGhQm7lvagee5Wf+Tg58PPlQeLAksL6X5f
zsnv7YFZOM77Llf5WJM9/uhJPALGq31699W1wbid0q7BTFBanwxZHBPpbivUPB1+
bVHQRpRzOhyPqo5/FdJ6+SPsZ/e9h809qKLgqDP9qX8H1lcvyvWev8+63JmTWxJx
d5+J4fOZzfdOqH7D7gqSKlS1f9QX/9mfsiy4PnXZ3lQm1C4l8n1t9iHcM7Cv1hVA
FELsLWTUVUPhn9BgWaIqbq+oSHzaJfWexys7v9dtO0ndO7uFKm8T2hHMFh5mkwkz
jd/dD10CgYEA9J7Q+dc1haY3+DQXHDThhEh2iFyOFWVj3V2a7PCLBqy71CxHr9XR
qVakwiG6Q1Bnwz/XmjKUWq3veXkVErmZOAABU+HIFA9QAO56cTRyyfNO5NTilE30
VE20rf+zGOupyidMXfKS2rAjfK9RPY/48eKlT8mWj4oEIRIatTUQ9dMCgYEA2Upi
ddMcXTNMDIVe9pDGLSljixlU3EizQPmRczlC/tAC/VAPqqr6FPHrxWF45qhpQAIV
m+zqHG4Tlsq9GMI0QjgAwKRoj/LTJNsejxPKWw2m70XC0N/7OqrOENdNBmtTA1vD
MIuBU3t3u/apGNoAXq2Lzi/qAzxF5wz8nvf8zV8CgYB8ft+IZ/j7Xg8aKRih6F/l
/SMmX0SIqyNaJCuW7w0yhnLJlwec+8tKzafojVXIsIE+o51NAvTx+ZfpULBi6UaL
c6U5Va2IWAq1jqmON8077rJ2T8pJBCuXRDzyWTKDOl0dX0bEgZIv7nkBGhDUrhNa
t6i+pLAVuX5EfnxNQQaytQKBgB0MJZdsrlkDN4Jg/e3mMqfs5YK90ytTiKsB8eC+
YedgdVXZsw50ptPP912+hwQGtXM6FBtxE2bTjEjXN2os5AGKLQeTsuqzYmiF5lLo
KV/8tjk8USvNFW+lT8DOl1xpUoKbbL97lsFLOxlkgvxwgCYn+w2IODdQgmO9x7OU
oTXvAoGAa1tJJy74pmt1INKATcDst9nJzZ0KqV6p9nFXwWwdjpv+qvc3JQ90LtJN
dYFLGEzMhp1zi5fSez4SoA6m574UgLOJCZSwWMXyC02a5THmRpCzLQ8ZZfHFEyie
QD+oEewAG5ucttPsaj2iK9YI3RonLcuQGaFuvRqsAuNWMwQyDtM=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_2: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_2: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
