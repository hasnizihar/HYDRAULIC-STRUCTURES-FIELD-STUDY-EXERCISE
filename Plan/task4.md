Yes. **Do not ask the user to guess those four values yet.** The agent should first perform a targeted source/data hunt. And I would change one important thing: **do not assume a “Sri Lanka Irrigation Department design gradient” unless the agent actually finds a source supporting 0.0004 for this specific canal/class of canal.**

Send this next prompt:

Before asking me to provide or confirm any missing values, perform a **targeted evidence search** to obtain the four missing Manning inputs for Site B.

The objective is:

**Use verified available data first → derive from reliable evidence where defensible → only then identify unavoidable assumptions.**

Do NOT ask me to guess engineering dimensions.

---

# TARGET PARAMETERS

Find evidence for:

1. Downstream canal bottom width, **b**
2. Total bank/channel depth, **H_bank**
3. Normal operating flow depth, **y**
4. Longitudinal bed slope, **S₀**

---

# 1. SEARCH THE EXISTING PROJECT FILES FIRST

Before using the internet, thoroughly inspect:

* Site B photographs
* Site B engineering sketches
* Site B preliminary report
* QA.md
* Q/A.md
* task1.md
* task3.md
* assignment guidelines
* map PDFs
* Google Maps data
* any notes, measurements or documents
* any previously generated research files

Search for:

* canal width
* channel width
* bottom width
* bank height
* canal depth
* water depth
* flow depth
* bed slope
* gradient
* invert level
* elevation
* longitudinal section
* canal section
* command canal
* branch canal
* Pulukunawa
* Vammiyadiyuttu
* Unnichchai
* irrigation canal

Do not rely only on filenames. Inspect the actual contents.

---

# 2. SEARCH THE INTERNET

If the values are not available in the project files, conduct a targeted web search.

Search specifically for the **actual irrigation system connected to Site B**, not generic Sri Lankan canals.

Search combinations such as:

* "Pulukunawa Reservoir canal dimensions"
* "Pulukunawa irrigation canal Batticaloa"
* "Pulukunawa irrigation scheme canal"
* "Vammiyadiyuttu irrigation canal"
* "Vammiyadiyuttu canal Batticaloa"
* "40th village irrigation canal Batticaloa"
* "Mandur irrigation canal Batticaloa"
* "Pulukunawa reservoir irrigation Batticaloa PDF"
* "Pulukunawa tank irrigation Batticaloa PDF"
* "Pulukunawa canal design Sri Lanka"
* "Pulukunawa irrigation scheme report"
* "Batticaloa irrigation scheme branch canal design"
* "Batticaloa Irrigation Department canal cross section PDF"
* "Unnichchai irrigation canal design Batticaloa"
* "Unnichchai right bank canal dimensions"
* "Unnichchai irrigation scheme technical report"

Also search:

* Google Scholar
* Sri Lankan university repositories
* Irrigation Department publications
* Mahaweli Authority publications
* Ministry of Irrigation reports
* District irrigation reports
* technical feasibility studies
* rehabilitation reports
* project appraisal reports
* environmental assessment reports
* tender documents
* engineering drawings
* scanned government reports

---

# 3. SEARCH FOR MAP/ELEVATION DATA

For **S₀**, investigate whether a defensible longitudinal slope can be derived from elevation data.

Possible sources:

* Survey Department maps
* official topographic maps
* DEM data
* Google Earth elevation
* SRTM
* ALOS
* GIS datasets
* engineering survey documents

If deriving slope:

S₀ = Δz / L

Record:

* upstream elevation
* downstream elevation
* horizontal distance
* resulting slope
* data source
* uncertainty

Do NOT call a regional gradient an actual canal bed slope.

---

# 4. USE THE PHOTOGRAPHS INTELLIGENTLY

Review the field photographs for dimensional references.

Potential reference objects include:

* student height
* gate width
* gate opening
* concrete chamber dimensions
* known masonry dimensions
* road/culvert dimensions
* structural widths already measured in the sketch

If a photograph allows a reasonable proportional estimate:

1. Explain the reference dimension.
2. Explain the measurement method.
3. Calculate the estimated dimension.
4. Label it:

**PHOTO-DERIVED ESTIMATE**

Do not present it as a field measurement.

If the photograph does not provide a reliable scale, mark the parameter as unavailable.

---

# 5. DO NOT INVENT WATER DEPTH

For **normal operating flow depth y**, search for:

* irrigation operation manuals
* canal design reports
* canal cross-sections
* water-level records
* field photographs during operation
* canal inspection reports
* design drawings
* irrigation department documents

If no reliable normal operating depth is found, do NOT arbitrarily select 0.8, 1.0 or 1.2 m.

Instead investigate whether we can perform a **bankfull hydraulic capacity analysis**.

---

# 6. BANKFULL ANALYSIS

If normal operating depth is unavailable, determine whether the available channel geometry supports a bankfull calculation.

Use:

**H_bank - freeboard = design flow depth**

BUT:

Do not automatically assume 0.3 m freeboard.

Find an engineering source supporting the selected freeboard for the relevant type of irrigation canal.

If no reliable source is available, present several scenarios rather than pretending one is the actual design value.

For example:

* Scenario A: conservative operating depth
* Scenario B: intermediate depth
* Scenario C: bankfull depth

Clearly label them as **analytical scenarios**, not observed conditions.

---

# 7. MANNING'S n

Do not blindly use 0.027–0.033.

First identify the actual channel condition:

* earth bed
* grass-covered banks
* weeds
* irregular section
* stone pitching near structure
* sediment/debris
* maintenance condition

Then consult a recognized hydraulic reference such as:

* Chow
* USACE
* USBR
* FHWA
* other recognized hydraulic engineering references

Select a defensible n.

Report:

**Selected n**

**Possible range**

**Reference**

**Reason for selection**

---

# 8. SOURCE PRIORITY

Use this hierarchy:

### Tier 1

Official engineering drawings / Irrigation Department documents

### Tier 2

Government technical reports

### Tier 3

University research / theses

### Tier 4

Peer-reviewed research

### Tier 5

Reliable GIS/topographic datasets

### Tier 6

Satellite/DEM-derived measurements

### Tier 7

Photographic estimates

### Tier 8

General engineering assumptions

Do not use Tier 8 if a better source exists.

---

# 9. IF A VALUE CANNOT BE FOUND

Do NOT fabricate it.

For every unavailable parameter, write:

**NOT FOUND IN AVAILABLE EVIDENCE**

Then determine whether the parameter can be:

A. Derived from another verified measurement

B. Estimated from a photograph

C. Derived from GIS/topographic data

D. Treated as a scenario variable

E. Omitted from the final calculation

Use the first defensible option available.

---

# 10. CREATE AN EVIDENCE TABLE

Before calculating Manning's equation, produce:

| Parameter      | Value | Unit | Source | Method                               | Confidence |
| -------------- | ----: | ---- | ------ | ------------------------------------ | ---------- |
| Bottom width b |       | m    |        | Field / Drawing / Photo / Literature |            |
| Bank height    |       | m    |        |                                      |            |
| Normal depth y |       | m    |        |                                      |            |
| Bed slope S₀   |       | m/m  |        |                                      |            |
| Manning n      |       | —    |        |                                      |            |

Also provide a short explanation for each value.

---

# 11. CONFIDENCE CLASSIFICATION

Use:

**HIGH**
Directly measured, official drawing, official engineering report.

**MEDIUM**
Reliable academic/technical source or defensible GIS-derived value.

**LOW**
Photographic estimate or secondary source.

**ASSUMED**
Engineering assumption used only because no actual value exists.

The final calculation must clearly identify any assumed inputs.

---

# 12. FINAL DECISION RULE

After the search:

### If all four values are found:

Proceed to Manning calculation.

### If some values are found:

Calculate using the verified values and clearly identify remaining assumptions.

### If critical values are unavailable:

Do NOT force a single numerical answer.

Instead perform a **scenario/sensitivity analysis** and state exactly what field measurement would be required to obtain the actual capacity.

---

# 13. IMPORTANT CORRECTION

Do NOT use:

> S₀ = 0.0004

simply because it is described as a "typical Sri Lanka Irrigation Department gradient."

That value must have an actual supporting source.

Likewise, do not automatically use:

> b = 3.0 m
> H_bank = 1.8 m
> y = 1.0 m
> n = 0.030

unless each is supported or explicitly labelled as an assumption.

---

## START NOW

Perform the evidence search and return:

### A. Existing project-file evidence

### B. Internet evidence

### C. Derived values

### D. Unavailable values

### E. Recommended calculation inputs

### F. Confidence assessment

**Do not ask me for measurements until this entire evidence search has been completed.**
