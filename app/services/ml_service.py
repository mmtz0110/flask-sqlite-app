class MLService:
    @staticmethod
    def predict_stunting(
        usia_bulan: int,
        berat_badan: float,
        tinggi_badan: float,
        jenis_kelamin: int,
    ) -> tuple[str, float]:
        """Return a placeholder classification until a validated model is integrated."""
        del berat_badan, jenis_kelamin
        tb_min_normal = 50 + (usia_bulan * 0.7)

        if tinggi_badan < tb_min_normal - 4:
            return "Sangat Pendek (Severely Stunted)", 6.0
        if tinggi_badan < tb_min_normal:
            return "Pendek (Stunted)", 3.5
        return "Normal", 0.0
