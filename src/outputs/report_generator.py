# src/outputs/report_generator.py
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ReportGenerator:
    def generate(self, trends, output_path):
        df = pd.DataFrame(trends).T
        df.to_csv(os.path.join("logs", "search_metrics.csv"))
        self._generate_html(df, output_path)
        logger.info(f"Report generated at {output_path}")

    def _generate_html(self, df, output_path):
        html = df.to_html()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"<h1>Search Monitor Report</h1>{html}")