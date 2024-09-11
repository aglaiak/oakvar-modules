from oakvar import BaseAnnotator
import sqlite3
class Annotator(BaseAnnotator):
    def annotate(self, input_data, secondary_data=None):
        _ = secondary_data

        if not self.cursor:           
            return None

        ref_base = input_data["ref_base"]
        alt_base = input_data["alt_base"]

        if len(ref_base) == len(alt_base) == 1 and ref_base != '-' and alt_base != '-':
            table = "SNVs"
        else:
            table = "INDELs"

        q = f"SELECT samples, qvalue, log10_pvalue FROM {table} WHERE hugo_symbol = '{input_data['hugo']}' AND base_achange= '{input_data['achange']}'"

        self.cursor.execute(q)
        row = self.cursor.fetchone()
        if row:
            samples, qvalue, log10_pvalue = row
            out = {"samples": samples, "qvalue": qvalue, "pvalue" : log10_pvalue}
        else:
            out = None
        return out
