"""Deterministic synthetic demo-data generator; safe to rerun in development."""
from random import Random
COUNTRIES=["United States","Mexico","Canada","India","China","Germany","Poland"]
COMMODITIES=["Sheet Metal","Structural Fabrication","Stamping","CNC Machining","Injection Molding","Die Casting","Welding","Assembly"]
DEMO_USERS=["admin","manager","buyer","analyst","executive","supplier"]
def generate(seed=2026):
 r=Random(seed)
 suppliers=[{"code":f"SUP-{1001+i}","name":f"Synthetic {['Forge','Precision','Industrial','Mobility','Fabrication'][i%5]} {i+1}","country":COUNTRIES[i%len(COUNTRIES)],"risk":r.randint(12,82)} for i in range(30)]
 suppliers[0].update(name="Apex Forge Systems",risk=68); suppliers[13].update(name="Northstar Fabrication",risk=22); suppliers[21].update(name="Great Lakes Precision",risk=31)
 return {"users":[f"{u}@sourcetwin.demo" for u in DEMO_USERS],"suppliers":suppliers,"components":[{"part_number":f"CMP-{i+1:03}","commodity":COMMODITIES[i%8]} for i in range(100)],"programs":[f"Synthetic Program {i+1}" for i in range(5)],"rfqs":[f"RFQ-2026-{i+1:03}" for i in range(10)]}
if __name__=="__main__":
 d=generate(); print(f"Generated {len(d['suppliers'])} suppliers, {len(d['components'])} components, {len(d['rfqs'])} RFQs")
