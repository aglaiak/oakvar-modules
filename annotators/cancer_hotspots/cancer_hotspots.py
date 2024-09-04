from oakvar import BaseAnnotator


class Annotator(BaseAnnotator):
    def annotate(self, input_data, secondary_data=None):
        _ = secondary_data
        if not self.cursor:            
            return None
        table = "SNVs"
        q = 'SELECT samples, qvalue, log10_pvalue FROM {table} WHERE hugo = {hugo} AND aachange = {aachange}'.format(
            
            hugo = input_data["hugo_symbol"],
            aachange = input_data["base_achange"],
            ref = input_data["base_achange"]
        )
        if not input_data["aachange"]:
            table = "INDELs"

        self.cursor.execute(q)
        row = self.cursor.fetchone()
        out = {"samples": samples, "qvalue": qvalue, "pvalue" : pvalue}

        return out
