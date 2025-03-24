from locust import HttpUser, task, between
import json
from datetime import datetime

# Data yang diberikan
data = [
    {"npwp": "960142899675294", "name": "SIT SCREENS SATUY", "dob": "09/05/1977"},
    {"npwp": "938018230939520", "name": "SIT SCREENS DUAY", "dob": "09/03/2005"},
    {"npwp": "947879318436959", "name": "SIT SCREENS TIGAY", "dob": "03/12/1997"},
    {"npwp": "940132767196744", "name": "SIT SCREENS EMPATY", "dob": "08/12/1983"},
    {"npwp": "996215255664526", "name": "SIT SCREENS LIMAY", "dob": "03/12/1997"},
    {"npwp": "955342024337179", "name": "SIT SCREENS ENAMY", "dob": "02/02/1978"},
    {"npwp": "924448418415817", "name": "SIT SCREENS TUJUHY", "dob": "09/03/1972"},
    {"npwp": "927049195851705", "name": "SIT SCREENS DELAPANY", "dob": "06/08/1976"},
    {"npwp": "963021468717695", "name": "SIT SCREENS SEMBILANY", "dob": "01/10/1973"},
    {"npwp": "988016300151071", "name": "SIT SCREENS SEPULUHY", "dob": "03/11/2002"},
    {"npwp": "992890180148872", "name": "SIT SCREENS SEBELASY", "dob": "04/11/1974"},
    {"npwp": "962186415898825", "name": "SIT SCREENS DUA BELASY", "dob": "07/03/1989"},
    {"npwp": "917488547977508", "name": "SIT SCREENS TIGA BELASY", "dob": "04/05/1980"},
    {"npwp": "913719745364001", "name": "SIT SCREENS EMPAT BELASY", "dob": "09/11/1991"},
    {"npwp": "967183460860481", "name": "SIT SCREENS LIMA BELASY", "dob": "01/12/1993"},
    {"npwp": "913634844415414", "name": "SIT SCREENS ENAM BELASY", "dob": "08/11/1975"},
    {"npwp": "932290048163871", "name": "SIT SCREENS TUJUH BELASY", "dob": "09/11/1991"},
    {"npwp": "968770747644030", "name": "SIT SCREENS DELAPAN BELASY", "dob": "04/01/2005"},
    {"npwp": "915458438443294", "name": "SIT SCREENS SEMBILAN BELASY", "dob": "08/06/1994"},
    {"npwp": "996620405420172", "name": "SIT SCREENS DUA PULUHY", "dob": "09/11/1991"},
    {"npwp": "943717724856954", "name": "SIT SCREENS DUA PULUH SATUY", "dob": "09/11/1991"},
    {"npwp": "915213866297138", "name": "SIT SCREENS DUA PULUH DUAY", "dob": "09/11/1991"},
    {"npwp": "960361019372006", "name": "SIT SCREENS DUA PULUH TIGAY", "dob": "06/03/2001"},
    {"npwp": "999002986334580", "name": "SIT SCREENS DUA PULUH EMPATY", "dob": "09/11/1991"},
    {"npwp": "941777872325671", "name": "SIT SCREENS DUA PULUH LIMAY", "dob": "04/12/1989"},
    {"npwp": "950826495988253", "name": "SIT SCREENS DUA PULUH ENAMY", "dob": "09/11/1991"},
    {"npwp": "942802524696310", "name": "SIT SCREENS DUA PULUH TUJUHY", "dob": "07/05/2003"},
    {"npwp": "986770817859757", "name": "SIT SCREENS DUA PULUH DELAPANY", "dob": "09/11/1991"},
    {"npwp": "998021623203139", "name": "SIT SCREENS DUA PULUH SEMBILANY", "dob": "01/04/1993"},
    {"npwp": "922617608944457", "name": "SIT SCREENS TIGA PULUHY", "dob": "09/11/1991"},
    {"npwp": "912381083143701", "name": "SIT SCREENS TIGA PULUH SATUY", "dob": "09/11/1991"},
    {"npwp": "968493483962924", "name": "SIT SCREENS TIGA PULUH DUAY", "dob": "09/11/1991"},
    {"npwp": "920671199944610", "name": "SIT SCREENS TIGA PULUH TIGAY", "dob": "09/11/1991"},
    {"npwp": "985669780476234", "name": "SIT SCREENS TIGA PULUH EMPATY", "dob": "09/11/1991"},
    {"npwp": "962620923473842", "name": "SIT SCREENS TIGA PULUH LIMAY", "dob": "07/05/2003"},
    {"npwp": "941025857069941", "name": "SIT SCREENS TIGA PULUH ENAMY", "dob": "07/05/2003"},
    {"npwp": "995523012404201", "name": "SIT SCREENS TIGA PULUH TUJUHY", "dob": "07/05/2003"},
    {"npwp": "921121514461251", "name": "SIT SCREENS TIGA PULUH DELAPANY", "dob": "07/05/2003"},
    {"npwp": "927115100068890", "name": "SIT SCREENS TIGA PULUH SEMBILANY", "dob": "06/04/1991"},
    {"npwp": "951607258330755", "name": "SIT SCREENS EMPAT PULUHY", "dob": "05/08/1994"},
    {"npwp": "927778251445750", "name": "SIT SCREENS EMPAT PULUH SATUY", "dob": "09/11/1991"},
    {"npwp": "989046085836281", "name": "SIT SCREENS EMPAT PULUH DUAY", "dob": "09/11/1991"},
    {"npwp": "977668469904843", "name": "SIT SCREENS EMPAT PULUH TIGAY", "dob": "01/03/1999"},
    {"npwp": "933278136214305", "name": "SIT SCREENS EMPAT PULUH EMPATY", "dob": "01/10/2001"},
    {"npwp": "982215161013270", "name": "SIT SCREENS EMPAT PULUH LIMAY", "dob": "09/11/1991"},
    {"npwp": "962706919722906", "name": "SIT SCREENS EMPAT PULUH ENAMY", "dob": "04/10/1972"},
    {"npwp": "961028001267242", "name": "SIT SCREENS EMPAT PULUH TUJUHY", "dob": "07/12/1998"},
    {"npwp": "967873291011786", "name": "SIT SCREENS EMPAT PULUH DELAPANY", "dob": "04/10/1973"},
    {"npwp": "987762729209803", "name": "SIT SCREENS EMPAT PULUH SEMBILANY", "dob": "09/11/1991"},
    {"npwp": "945523017934440", "name": "SIT SCREENS LIMA PULUHY", "dob": "09/11/1991"},
    {"npwp": "927891702293356", "name": "SIT SCREENS LIMA PULUH SATUY", "dob": "03/02/1973"},
    {"npwp": "928398344623651", "name": "SIT SCREENS LIMA PULUH DUAY", "dob": "09/11/1991"},
    {"npwp": "954404112217692", "name": "SIT SCREENS LIMA PULUH TIGAY", "dob": "09/11/1991"},
    {"npwp": "940246947434946", "name": "SIT SCREENS LIMA PULUH EMPATY", "dob": "04/10/1990"},
    {"npwp": "990966212504111", "name": "SIT SCREENS LIMA PULUH LIMAY", "dob": "03/10/1999"},
    {"npwp": "931126404031794", "name": "SIT SCREENS LIMA PULUH ENAMY", "dob": "07/05/2003"},
    {"npwp": "942418995584674", "name": "SIT SCREENS LIMA PULUH TUJUHY", "dob": "07/05/2003"},
    {"npwp": "916627272538798", "name": "SIT SCREENS LIMA PULUH DELAPANY", "dob": "07/05/2003"},
    {"npwp": "912785197541440", "name": "SIT SCREENS LIMA PULUH SEMBILANY", "dob": "07/05/2003"},
    {"npwp": "986675215403363", "name": "SIT SCREENS ENAM PULUHY", "dob": "07/05/2003"},
    {"npwp": "946091525814391", "name": "SIT SCREENS ENAM PULUH SATUY", "dob": "07/05/2003"},
    {"npwp": "954815857387107", "name": "SIT SCREENS ENAM PULUH DUAY", "dob": "07/05/2003"},
    {"npwp": "968912988990915", "name": "SIT SCREENS ENAM PULUH TIGAY", "dob": "07/05/2003"},
    {"npwp": "918346206269272", "name": "SIT SCREENS ENAM PULUH EMPATY", "dob": "06/07/1995"},
    {"npwp": "917330076583130", "name": "SIT SCREENS ENAM PULUH LIMAY", "dob": "07/05/2003"},
    {"npwp": "947565439695776", "name": "SIT SCREENS ENAM PULUH ENAMY", "dob": "07/10/1976"},
    {"npwp": "974833475270580", "name": "SIT SCREENS ENAM PULUH TUJUHY", "dob": "07/05/2003"},
    {"npwp": "985861511564148", "name": "SIT SCREENS ENAM PULUH DELAPANY", "dob": "07/05/2003"},
    {"npwp": "915601272227116", "name": "SIT SCREENS ENAM PULUH SEMBILANY", "dob": "07/05/2003"},
    {"npwp": "943120931589780", "name": "SIT SCREENS TUJUH PULUHY", "dob": "07/05/2003"},
    {"npwp": "949480002218891", "name": "SIT SCREENS TUJUH PULUH SATUY", "dob": "07/05/2003"},
    {"npwp": "968170888478408", "name": "SIT SCREENS TUJUH PULUH DUAY", "dob": "07/05/2003"},
    {"npwp": "933344955118369", "name": "SIT SCREENS TUJUH PULUH TIGAY", "dob": "07/05/2003"},
    {"npwp": "962148098782518", "name": "SIT SCREENS TUJUH PULUH EMPATY", "dob": "07/11/1988"},
    {"npwp": "932266107791608", "name": "SIT SCREENS TUJUH PULUH LIMAY", "dob": "07/05/2003"},
    {"npwp": "952448958394819", "name": "SIT SCREENS TUJUH PULUH ENAMY", "dob": "07/05/2003"},
    {"npwp": "934382547320052", "name": "SIT SCREENS TUJUH PULUH TUJUHY", "dob": "09/10/1992"},
    {"npwp": "975866290288479", "name": "SIT SCREENS TUJUH PULUH DELAPANY", "dob": "07/05/2003"},
    {"npwp": "946973449479100", "name": "SIT SCREENS TUJUH PULUH SEMBILANY", "dob": "06/04/1993"},
    {"npwp": "916096445883819", "name": "SIT SCREENS DELAPAN PULUHY", "dob": "07/05/2003"},
    {"npwp": "993312821010962", "name": "SIT SCREENS DELAPAN PULUH SATUY", "dob": "07/05/2003"},
    {"npwp": "990898674942585", "name": "SIT SCREENS DELAPAN PULUH DUAY", "dob": "07/05/2003"},
    {"npwp": "999308093463733", "name": "SIT SCREENS DELAPAN PULUH TIGAY", "dob": "07/05/2003"},
    {"npwp": "913605846662674", "name": "SIT SCREENS DELAPAN PULUH EMPATY", "dob": "07/05/2003"},
    {"npwp": "932769253304375", "name": "SIT SCREENS DELAPAN PULUH LIMAY", "dob": "06/06/1983"},
    {"npwp": "966098970985142", "name": "SIT SCREENS DELAPAN PULUH ENAMY", "dob": "04/07/1982"},
    {"npwp": "920945982635650", "name": "SIT SCREENS DELAPAN PULUH TUJUHY", "dob": "04/12/1998"},
    {"npwp": "920563490561083", "name": "SIT SCREENS DELAPAN PULUH DELAPANY", "dob": "05/07/1976"},
    {"npwp": "925993852161831", "name": "SIT SCREENS DELAPAN PULUH SEMBILANY", "dob": "08/06/1975"},
    {"npwp": "937123854228991", "name": "SIT SCREENS SEMBILAN PULUHY", "dob": "04/12/1975"},
    {"npwp": "928798768648804", "name": "SIT SCREENS SEMBILAN PULUH SATUY", "dob": "08/05/1991"},
    {"npwp": "991776725170587", "name": "SIT SCREENS SEMBILAN PULUH DUAY", "dob": "04/08/1979"},
    {"npwp": "944703189081874", "name": "SIT SCREENS SEMBILAN PULUH TIGAY", "dob": "01/06/1972"},
    {"npwp": "991434913472524", "name": "SIT SCREENS SEMBILAN PULUH EMPATY", "dob": "09/11/1992"},
    {"npwp": "991712390207239", "name": "SIT SCREENS SEMBILAN PULUH LIMAY", "dob": "07/08/1996"},
    {"npwp": "976951051070173", "name": "SIT SCREENS SEMBILAN PULUH ENAMY", "dob": "09/05/1993"},
    {"npwp": "924317346171588", "name": "SIT SCREENS SEMBILAN PULUH TUJUHY", "dob": "05/07/1971"},
    {"npwp": "933784754506703", "name": "SIT SCREENS SEMBILAN PULUH DELAPANY", "dob": "04/02/1997"},
    {"npwp": "918874768311187", "name": "SIT SCREENS SEMBILAN PULUH SEMBILANY", "dob": "08/05/1981"},
    {"npwp": "955542963544984", "name": "SIT SCREENS SERATUSY", "dob": "02/11/1995"}
]






# Fungsi untuk mengubah format tanggal dari DD/MM/YYYY ke YYYY-MM-DD
def format_date(dob):
    return datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")

class ApiUser(HttpUser):
    wait_time = between(1, 2)  # Waktu tunggu antar request (1-2 detik)

    @task
    def fraud_checking(self):
        for record in data:
            # Format tanggal lahir menjadi YYYY-MM-DD
            formatted_dob = format_date(record["dob"])

            # Payload JSON
            payload = {
                "config": {
                    "sourceRequest": "Legacy Corporate",
                    "screeningApuppt": True
                },
                "screeningAPUPPT": {
                    "name": record["name"],
                    "idNumber": record["npwp"],
                    "idType": "NPWP",
                    "dob": formatted_dob
                }
            }

            # Kirim POST request
            with self.client.post(
                "/v2/ao-fraud/workflow/fraud-checking",
                headers={
                    "apiKey": "E97baCBt8SxmDcYNyd3KwbEA0giw8ElF",
                    "Content-Type": "application/json",
                },
                data=json.dumps(payload),
                catch_response=True,
            ) as response:
                # Anggap status 200 dan 201 sebagai sukses
                if response.status_code in [200, 201]:
                    response.success()
                else:
                    response.failure(f"Failed with status code {response.status_code}")
