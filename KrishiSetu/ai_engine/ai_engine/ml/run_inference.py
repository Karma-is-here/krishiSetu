import pandas as pd
from ml.windowing.window_builder import build_windows
from ml.experts.vegetation_expert import VegetationExpert
from ml.experts.rainfall_expert import RainfallExpert
from ml.experts.soil_expert import SoilExpert
from ml.experts.temperature_expert import TemperatureExpert
from ml.fusion.fusion_model import FusionModel
from ml.hashing.input_hasher import hash_input
from ml.decision.decision_vector import build
from ml.confidence.confidence_estimator import estimate

df = pd.read_csv(
    "data_ingestion/data/features/features_weekly.csv",
    parse_dates=["week"]
)

feature_cols = [c for c in df.columns if c not in ["lat", "lon", "week"]]

experts = {
    "vegetation": VegetationExpert(),
    "rainfall": RainfallExpert(),
    "soil": SoilExpert(),
    "temperature": TemperatureExpert()
}

fusion = FusionModel()

windows, meta = build_windows(df, feature_cols, window_size=8)

decisions = []

for w, m in zip(windows, meta):
    scores, confs = {}, []

    for name, expert in experts.items():
        s, c = expert.predict(w)
        scores[name] = s
        confs.append(c)

    stress = fusion.fuse(scores)
    confidence = estimate(confs)

    decisions.append({
        **m,
        "decision": build(stress, confidence, scores),
        "input_hash": hash_input(w)
    })

print("Decisions generated:", len(decisions))
