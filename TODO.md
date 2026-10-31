# Outstanding work

## Fast local checks and complete CI acceptance

Local hooks reject basic defects in the actual changed content; CI owns full test suites,
corpus-wide validation, builds, rendering, and broad audits. QC-01 through QC-05 and
QC-07 through QC-11 are closed. Two items remain open.

| ID | Task | Needs |
| --- | --- | --- |
| QC-06 | Run the complete shared acceptance tier in hosted CI | none |
| QC-12 | Close the workstream against a complete hosted run | QC-06 |

- [ ] **QC-06 — Wire the hosted acceptance tier for this repository's workflow.**
  **Owner:** ai-review-ci's supported workflow integration and `.github/workflows/`.
  The hosted workflows are `development.yml` (build, link crawl, deploy, and the
  `corpus-reports` job) and `ambient.yml` (the shared `_qc.yml` workflow). The shared
  reusable workflow runs all diagnostics and can either report their failures or enforce
  all of them; it has no supported result that enforces only the test suite. The full
  doctor reports a missing PR workflow and branch protection. Determine the supported
  integration for the repository's direct-to-main policy before changing repository
  protection or requiring PRs. Full acceptance needs the Python, Pandoc, LaTeX, and filter
  dependencies, must not inherit the local pytest file selection, and must not run the
  complete suite twice.
  **Acceptance:** a hosted run demonstrates execution of the complete intended acceptance
  tier, with a real comparison base for diff checks and explicit failure propagation.
  Any workflow-policy decision still requiring owner choice is stated before changing it.

- [ ] **QC-12 — Close against the full completion condition.**
  Verify a single current revision through hosted acceptance, report publication, site
  build, crawl, and deployment. Confirm the deployed revision stamp. Reconcile resolved
  complaint entries with the delivered state.
  **Acceptance:** cheap errors are caught locally; expensive checks run in CI; generated
  reports are usable; remaining failures are explicitly owned. Successful local hooks
  alone do not close this workstream.

## Execution DAG

A prerequisite `A` on task `B` means `A -> B`. `none` denotes a ready root.
Before committing a dependency change, verify unique IDs, resolved references, and absence of cycles.
Closed nodes are not executable work; their evidence is in Git history.
For a newly selected repair, name its card or issue ID, its immediate Needs and its acceptance
beside the existing items, and link its complaint.

Read [CONTRIBUTING.md](CONTRIBUTING.md#named-policies) and record issues as they arise in [COMPLAINTS.md](COMPLAINTS.md).

### Current route

`publication-milestone`, `unsolved-contribution`, `slogans`, `lamport-conversion`,
`solution-section-restoration`, and `copy-policy-repair` are closed. The next ready node is
`audited-deployment`.

Copy is reader-facing prose: wiki pages, remarks, and site strings. Problem statements and
proofs are mathematics, not copy. A defect in a statement or proof is repaired as a
mathematical correction under its own node, not under copy policy.

- **`audited-deployment`**. **Needs:** none. Read the whole site content in its source form
  (collection cards, the problem cards they list, and wiki markdown) against the source PDFs and
  extractions, the [CONTRIBUTING.md](CONTRIBUTING.md#policy-families) policies, and the
  mathematics. Check for incorrect facts, statements, and solutions; it is a reading, not a lint
  or crawl count. A reader fixes each defect in place and commits it with the item; only a
  defect the reader cannot repair becomes a node in this DAG, named by its card or page, and
  `audited-deployment` gains it as a prerequisite. Nothing waits for a deploy: ordinary pushes
  deploy the repairs, and a rendering-only defect is checked on whatever revision is live.
  **Acceptance:** every item of the reading checklist below is ticked and every injected node is
  closed. Rounds 1-9 sampled slices without recording coverage, so the checklist starts
  unticked.
  Round 1 (revision `fe928e9a1`) injected the nodes below; `audited-deployment` needs all of them.

  Reading checklist. Each item is read once, in full, against its source; its repairs are
  committed before the item is ticked.
  Collections (the collection page and every problem page it lists):
  - [x] SRC-AG-EXAM-PROBLEMS-2015
  - [x] SRC-AG-HOMEWORK
  - [x] SRC-AGX-MISC-AG-PROBLEMS
  - [x] SRC-AGX-VARIETIES-PROBLEMS
  - [x] SRC-ALG-ART-HEACCB
  - [x] SRC-ALG-ART-PSET5-QUALS
  - [x] SRC-ALG-ART-QHGA3N
  - [x] SRC-ALG-ART-SEPT2019
  - [x] SRC-ALG-QUAL-WINTER-2018
  - [x] SRC-ALGEBRA-COMP-FALL-2003
  - [x] SRC-ALGEBRA-FINAL-2011-SOLUTIONS
  - [x] SRC-ALGEBRA-REVIEW-PANTANO-2011
  - [x] SRC-ALGEBRA-TEST-REVIEW-1
  - [x] SRC-AMHERST-ALGEBRA-STUDY-GUIDE-2016
  - [x] SRC-ART-ALG-2003-2009-PRELIMS
  - [x] SRC-ART-ALG-2010-2015-PRELIMS
  - [x] SRC-AZOFF-PROBLEMS-BY-TOPIC
  - [x] SRC-BASIC-LINEAR-ALGEBRA-REVIEW
  - [x] SRC-BERKELEY-MATH185-FALL-2009-PSET7
  - [x] SRC-BERKELEY-PRELIM-FALL-1977
  - [x] SRC-BERKELEY-PRELIM-FALL-1978
  - [x] SRC-BERKELEY-PRELIM-FALL-1979
  - [x] SRC-BERKELEY-PRELIM-FALL-1980
  - [x] SRC-BERKELEY-PRELIM-FALL-1981
  - [x] SRC-BERKELEY-PRELIM-FALL-1982
  - [x] SRC-BERKELEY-PRELIM-FALL-1983
  - [x] SRC-BERKELEY-PRELIM-FALL-1984
  - [x] SRC-BERKELEY-PRELIM-FALL-1985
  - [x] SRC-BERKELEY-PRELIM-FALL-1986
  - [x] SRC-BERKELEY-PRELIM-FALL-1987
  - [x] SRC-BERKELEY-PRELIM-FALL-1988
  - [x] SRC-BERKELEY-PRELIM-FALL-1989
  - [x] SRC-BERKELEY-PRELIM-FALL-1990
  - [x] SRC-BERKELEY-PRELIM-FALL-1991
  - [x] SRC-BERKELEY-PRELIM-FALL-1992
  - [x] SRC-BERKELEY-PRELIM-FALL-1993
  - [x] SRC-BERKELEY-PRELIM-FALL-1994
  - [x] SRC-BERKELEY-PRELIM-FALL-1995
  - [x] SRC-BERKELEY-PRELIM-FALL-1996
  - [x] SRC-BERKELEY-PRELIM-FALL-1997
  - [x] SRC-BERKELEY-PRELIM-FALL-1998
  - [x] SRC-BERKELEY-PRELIM-FALL-1999
  - [x] SRC-BERKELEY-PRELIM-FALL-2000
  - [x] SRC-BERKELEY-PRELIM-FALL-2003
  - [x] SRC-BERKELEY-PRELIM-FALL-2004
  - [x] SRC-BERKELEY-PRELIM-FALL-2005
  - [x] SRC-BERKELEY-PRELIM-FALL-2006
  - [x] SRC-BERKELEY-PRELIM-FALL-2007
  - [x] SRC-BERKELEY-PRELIM-FALL-2008
  - [x] SRC-BERKELEY-PRELIM-FALL-2009
  - [x] SRC-BERKELEY-PRELIM-FALL-2010
  - [x] SRC-BERKELEY-PRELIM-FALL-2011
  - [x] SRC-BERKELEY-PRELIM-FALL-2012
  - [x] SRC-BERKELEY-PRELIM-FALL-2013
  - [x] SRC-BERKELEY-PRELIM-FALL-2014
  - [x] SRC-BERKELEY-PRELIM-FALL-2015
  - [x] SRC-BERKELEY-PRELIM-FALL-2016
  - [x] SRC-BERKELEY-PRELIM-FALL-2018
  - [x] SRC-BERKELEY-PRELIM-FALL-2020
  - [x] SRC-BERKELEY-PRELIM-SPRING-1977
  - [x] SRC-BERKELEY-PRELIM-SPRING-1978
  - [x] SRC-BERKELEY-PRELIM-SPRING-1979
  - [x] SRC-BERKELEY-PRELIM-SPRING-1980
  - [x] SRC-BERKELEY-PRELIM-SPRING-1981
  - [x] SRC-BERKELEY-PRELIM-SPRING-1982
  - [x] SRC-BERKELEY-PRELIM-SPRING-1983
  - [x] SRC-BERKELEY-PRELIM-SPRING-1984
  - [x] SRC-BERKELEY-PRELIM-SPRING-1985
  - [x] SRC-BERKELEY-PRELIM-SPRING-1986
  - [x] SRC-BERKELEY-PRELIM-SPRING-1987
  - [x] SRC-BERKELEY-PRELIM-SPRING-1988
  - [x] SRC-BERKELEY-PRELIM-SPRING-1989
  - [x] SRC-BERKELEY-PRELIM-SPRING-1990
  - [x] SRC-BERKELEY-PRELIM-SPRING-1991
  - [x] SRC-BERKELEY-PRELIM-SPRING-1992
  - [x] SRC-BERKELEY-PRELIM-SPRING-1993
  - [x] SRC-BERKELEY-PRELIM-SPRING-1994
  - [x] SRC-BERKELEY-PRELIM-SPRING-1995
  - [x] SRC-BERKELEY-PRELIM-SPRING-1996
  - [x] SRC-BERKELEY-PRELIM-SPRING-1997
  - [x] SRC-BERKELEY-PRELIM-SPRING-1998
  - [x] SRC-BERKELEY-PRELIM-SPRING-1999
  - [x] SRC-BERKELEY-PRELIM-SPRING-2000
  - [x] SRC-BERKELEY-PRELIM-SPRING-2001
  - [x] SRC-BERKELEY-PRELIM-SPRING-2003
  - [x] SRC-BERKELEY-PRELIM-SPRING-2004
  - [x] SRC-BERKELEY-PRELIM-SPRING-2005
  - [x] SRC-BERKELEY-PRELIM-SPRING-2006
  - [x] SRC-BERKELEY-PRELIM-SPRING-2007
  - [x] SRC-BERKELEY-PRELIM-SPRING-2008
  - [x] SRC-BERKELEY-PRELIM-SPRING-2009
  - [x] SRC-BERKELEY-PRELIM-SPRING-2010
  - [x] SRC-BERKELEY-PRELIM-SPRING-2011
  - [x] SRC-BERKELEY-PRELIM-SPRING-2012
  - [x] SRC-BERKELEY-PRELIM-SPRING-2013
  - [x] SRC-BERKELEY-PRELIM-SPRING-2014
  - [x] SRC-BERKELEY-PRELIM-SPRING-2015
  - [x] SRC-BERKELEY-PRELIM-SPRING-2016
  - [x] SRC-BERKELEY-PRELIM-SPRING-2017
  - [x] SRC-BERKELEY-PRELIM-SPRING-2019
  - [x] SRC-BERKELEY-PRELIM-SPRING-2021
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1977
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1978
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1979
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1980
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1981
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1982
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1983
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1984
  - [x] SRC-BERKELEY-PRELIM-SUMMER-1985
  - [x] SRC-CA-ART-E3SXDB
  - [x] SRC-CA-ART-T34TG3
  - [x] SRC-CALCULUS-PRACTICE-TEST3
  - [x] SRC-CAMBRIDGE-COMPLEX-METHODS-LENT-2016
  - [x] SRC-CH10-HOMOMORPHISM-SOLUTION-OUTLINES
  - [x] SRC-CH10A-HOMOMORPHISM-SOLUTION-OUTLINES
  - [x] SRC-CH11-ABELIAN-GROUP-SOLUTION-OUTLINES
  - [x] SRC-CH12-RING-SOLUTION-OUTLINES
  - [x] SRC-CH13-RING-SOLUTION-OUTLINES
  - [x] SRC-CH14-IDEAL-SOLUTION-OUTLINES
  - [x] SRC-CH15-RING-HOMOMORPHISM-SOLUTION-OUTLINES
  - [x] SRC-CH16-POLYNOMIAL-RING-SOLUTION-OUTLINES
  - [x] SRC-CH17-POLYNOMIAL-SOLUTION-OUTLINES
  - [x] SRC-CH20-FIELD-SOLUTION-OUTLINES
  - [x] SRC-CH7-GROUP-SOLUTION-OUTLINES
  - [x] SRC-CH8-DIRECT-PRODUCT-SOLUTION-OUTLINES
  - [x] SRC-CH9-FACTOR-GROUP-SOLUTIONS
  - [x] SRC-CHAVAN-COMPLEX-PROBLEMS-2015
  - [x] SRC-COMPLEX-ANALYSIS-EXAM-PREP
  - [x] SRC-DUKE-BASIC-ANALYSIS-WINTER-2014
  - [x] SRC-EMORY-QUAL-PROBLEMS
  - [x] SRC-FIELDS-HOMEWORK-1
  - [x] SRC-GATHMANN-AG
  - [x] SRC-GRE-GR8767-CALCULUS-SELECTION
  - [x] SRC-GRE-MATH-SUBJECT
  - [x] SRC-HARVARD-MATH213A-2017
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-FINAL
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-1
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-6
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-7
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-8
  - [x] SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-9
  - [x] SRC-HARVARD-QUAL-SAMPLE-AG
  - [x] SRC-HARVARD-TATE-ALGEBRA-250A-1985
  - [x] SRC-JHU-ANALYSIS-EXAMS
  - [x] SRC-KENT-STATE-RING-THEORY-QUAL-2017
  - [x] SRC-LERMAN-ALGEBRA-REVIEW
  - [x] SRC-LINEAR-ALGEBRA-TEST2-REVIEW
  - [x] SRC-MA553-MIDTERM-I-SAMPLE-PROBLEMS
  - [ ] SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007
  - [x] SRC-MAT367-DIFFGEOM-2017
  - [ ] SRC-MATH113-SUMMER-2016-HW7
  - [ ] SRC-MATH114-GALOIS-HOMEWORK-2006
  - [x] SRC-MATH4100-6100-2020
  - [x] SRC-MATH504-FINAL-AUTUMN-2003
  - [ ] SRC-MATH6338-HW8
  - [ ] SRC-MATH655-HW3-2003
  - [ ] SRC-MATH7200-EXERCISE-SET-8-FALL-2006
  - [x] SRC-MATH8100-ASSIGNMENT-1
  - [x] SRC-MATH8100-ASSIGNMENT-2
  - [x] SRC-MATH8100-ASSIGNMENT-3
  - [x] SRC-MATH8100-ASSIGNMENT-4
  - [x] SRC-MATH8100-ASSIGNMENT-5
  - [x] SRC-MATH8100-ASSIGNMENT-6
  - [x] SRC-MATH8100-ASSIGNMENT-7
  - [x] SRC-MATH8100-ASSIGNMENT-8
  - [x] SRC-MATH8100-FALL-2019-ASSIGNMENTS
  - [ ] SRC-MATHEMATICAL-TRIVIUM
  - [ ] SRC-MAXIM-PROBLEMS-ALGEBRAIC-TOPOLOGY
  - [ ] SRC-MGSA-COMM-ALG-ORAL
  - [ ] SRC-MGSA-COMPLEX-ORAL
  - [ ] SRC-MGSA-FIELDS-ORAL
  - [ ] SRC-MGSA-GROUPS-ORAL
  - [ ] SRC-MTH674-DIFFGEOM-MIDTERM-SAMPLE
  - [ ] SRC-NORI-GALOIS-THEORY-PROBLEMS
  - [ ] SRC-NUS-CA-1970-SPRING
  - [ ] SRC-NUS-RA-1970-SPRING
  - [ ] SRC-PERUTZ-ALGEBRAIC-TOPOLOGY-I-2008
  - [ ] SRC-POINT-SET-TOPOLOGY-MIDTERM
  - [ ] SRC-PRELIM-ART-A2355I
  - [ ] SRC-PRELIM-ART-INTEGRAL-PRACTICE
  - [ ] SRC-PRELIM-CALCULUS-I-WEEK1
  - [ ] SRC-PRELIM-CALCULUS-II-WEEK2
  - [ ] SRC-PRELIM-PRACTICE-WEEK3-2020
  - [ ] SRC-PRELIM-PRACTICE-WEEK4-2020
  - [ ] SRC-PRELIM-PRACTICE-WEEK5-2020
  - [ ] SRC-PRELIM-PRACTICE-WEEK6-2020
  - [ ] SRC-QUAL-REVIEW-HATCHER
  - [ ] SRC-RA-WORKSHOP
  - [ ] SRC-SEQUENCES-SERIES-ASSIGNMENT-2
  - [ ] SRC-SHONKWILER-ALGEBRA-HW11
  - [ ] SRC-SHONKWILER-ALGEBRA-HW4
  - [ ] SRC-STANDREWS-MT5824-PSET7-2010
  - [ ] SRC-TAMU-RA-FALL-2014
  - [ ] SRC-TAMU-RA-FALL-2015
  - [ ] SRC-TAMU-RA-FALL-2016
  - [ ] SRC-TAMU-RA-SPRING-2015
  - [ ] SRC-TAMU-RA-SPRING-2016
  - [ ] SRC-TAMU-RA-SPRING-2017
  - [ ] SRC-TEXT-DF04
  - [ ] SRC-TEXT-FOL99
  - [ ] SRC-TEXT-HART77
  - [ ] SRC-TEXT-HAT02
  - [ ] SRC-TEXT-HK71
  - [ ] SRC-TEXT-HUN74
  - [ ] SRC-TEXT-MUN00
  - [ ] SRC-TEXT-RUD76
  - [ ] SRC-TEXT-SMI
  - [ ] SRC-TEXT-SS03
  - [ ] SRC-TEXT-SS03-FOURIER
  - [ ] SRC-TEXT-SS05
  - [ ] SRC-TOP-2002Q1
  - [ ] SRC-TOP-2011Q2
  - [ ] SRC-TOP-2012Q1
  - [ ] SRC-TOP-2012Q2
  - [x] SRC-TOP-2013Q2
  - [x] SRC-TOP-2015Q2
  - [x] SRC-TOP-2017Q2
  - [x] SRC-TOP-2018Q2
  - [x] SRC-TOP-2019Q1
  - [x] SRC-TOP-2019Q2
  - [x] SRC-TOP-2020Q1
  - [x] SRC-TOP-SQUAL1
  - [x] SRC-TOP-SQUAL2
  - [x] SRC-TOP-UNL-2005Q2
  - [x] SRC-TOP-UNL-2006Q1
  - [x] SRC-TOP-UNL-2006Q2
  - [x] SRC-TOP-UNL-2007Q2
  - [x] SRC-TOP-UNL-2008Q2
  - [x] SRC-TOP-UNL-2009Q2
  - [x] SRC-TOP-UNL-2010Q2
  - [x] SRC-TOP-UNL-2014Q2
  - [x] SRC-TOP-UNL-2016Q2
  - [x] SRC-TOP-UNL-2017Q1
  - [x] SRC-TOP-WORKSHOP
  - [x] SRC-TOP-WORKSHOP-2020
  - [x] SRC-TOPOLOGY-PHD-F07
  - [x] SRC-TOPOLOGY-PHD-F08
  - [x] SRC-TOPOLOGY-PHD-F95
  - [x] SRC-TOPOLOGY-SEPARATION-COUNTABILITY-REVIEW
  - [x] SRC-UCI-MATH220C-2013-HW3
  - [x] SRC-UCI-MATH220C-SPRING-2018-HW5
  - [x] SRC-UCLA-BASIC-FALL-2001
  - [x] SRC-UCLA-BASIC-FALL-2002
  - [x] SRC-UCLA-BASIC-FALL-2003
  - [x] SRC-UCLA-BASIC-FALL-2004
  - [x] SRC-UCLA-BASIC-FALL-2005
  - [x] SRC-UCLA-BASIC-FALL-2007
  - [x] SRC-UCLA-BASIC-FALL-2008
  - [x] SRC-UCLA-BASIC-FALL-2009
  - [x] SRC-UCLA-BASIC-FALL-2010
  - [x] SRC-UCLA-BASIC-FALL-2011
  - [x] SRC-UCLA-BASIC-FALL-2012
  - [x] SRC-UCLA-BASIC-FALL-2013
  - [x] SRC-UCLA-BASIC-FALL-2014
  - [x] SRC-UCLA-BASIC-FALL-2015
  - [x] SRC-UCLA-BASIC-FALL-2016
  - [x] SRC-UCLA-BASIC-FALL-2017
  - [x] SRC-UCLA-BASIC-FALL-2018
  - [x] SRC-UCLA-BASIC-SPRING-2002
  - [x] SRC-UCLA-BASIC-SPRING-2003
  - [x] SRC-UCLA-BASIC-SPRING-2004
  - [x] SRC-UCLA-BASIC-SPRING-2005
  - [x] SRC-UCLA-BASIC-SPRING-2006
  - [x] SRC-UCLA-BASIC-SPRING-2007
  - [x] SRC-UCLA-BASIC-SPRING-2008
  - [x] SRC-UCLA-BASIC-SPRING-2009
  - [x] SRC-UCLA-BASIC-SPRING-2010
  - [x] SRC-UCLA-BASIC-SPRING-2011
  - [x] SRC-UCLA-BASIC-SPRING-2013
  - [x] SRC-UCLA-BASIC-SPRING-2014
  - [x] SRC-UCLA-BASIC-SPRING-2015
  - [x] SRC-UCLA-BASIC-SPRING-2016
  - [x] SRC-UCLA-BASIC-SPRING-2017
  - [x] SRC-UCLA-BASIC-SPRING-2018
  - [x] SRC-UCLA-BASIC-WINTER-2002
  - [x] SRC-UCLA-BASIC-WINTER-2006
  - [x] SRC-UCLA-BASIC-WINTER-2012
  - [x] SRC-UCLA-RA-FALL-2009
  - [x] SRC-UCLA-RA-FALL-2010
  - [x] SRC-UCLA-RA-FALL-2011
  - [x] SRC-UCLA-RA-FALL-2012
  - [x] SRC-UCLA-RA-FALL-2013
  - [x] SRC-UCLA-RA-FALL-2014
  - [x] SRC-UCLA-RA-FALL-2015
  - [x] SRC-UCLA-RA-FALL-2016
  - [x] SRC-UCLA-RA-FALL-2017
  - [x] SRC-UCLA-RA-FALL-2018
  - [x] SRC-UCLA-RA-SPRING-2009
  - [x] SRC-UCLA-RA-SPRING-2010
  - [x] SRC-UCLA-RA-SPRING-2011
  - [x] SRC-UCLA-RA-SPRING-2012
  - [x] SRC-UCLA-RA-SPRING-2013
  - [x] SRC-UCLA-RA-SPRING-2014
  - [x] SRC-UCLA-RA-SPRING-2015
  - [x] SRC-UCLA-RA-SPRING-2016
  - [x] SRC-UCLA-RA-SPRING-2017
  - [x] SRC-UCLA-RA-SPRING-2018
  - [x] SRC-UCR-PIERCE-FUNDAMENTAL-ALGEBRA
  - [x] SRC-UCSD-ALG-200A-HOMEWORK
  - [x] SRC-UCSD-ALG-FALL-2006
  - [x] SRC-UCSD-ALG-FALL-2007
  - [x] SRC-UCSD-ALG-FALL-2008
  - [x] SRC-UCSD-ALG-FALL-2009
  - [x] SRC-UCSD-ALG-FALL-2010
  - [x] SRC-UCSD-ALG-FALL-2011
  - [x] SRC-UCSD-ALG-FALL-2013
  - [x] SRC-UCSD-ALG-FALL-2014
  - [x] SRC-UCSD-ALG-FALL-2017
  - [x] SRC-UCSD-ALG-FALL-2018
  - [x] SRC-UCSD-ALG-FALL-2019
  - [x] SRC-UCSD-ALG-FALL-2020
  - [x] SRC-UCSD-ALG-FALL-2021
  - [x] SRC-UCSD-ALG-FALL-2022
  - [x] SRC-UCSD-ALG-FALL-2023
  - [x] SRC-UCSD-ALG-FALL-2024
  - [x] SRC-UCSD-ALG-FALL-2025
  - [x] SRC-UCSD-ALG-REVIEW-FIELDS
  - [x] SRC-UCSD-ALG-REVIEW-GROUPS
  - [x] SRC-UCSD-ALG-REVIEW-RINGS-MODULES
  - [x] SRC-UCSD-ALG-SPRING-2004
  - [x] SRC-UCSD-ALG-SPRING-2005
  - [x] SRC-UCSD-ALG-SPRING-2006
  - [x] SRC-UCSD-ALG-SPRING-2007
  - [x] SRC-UCSD-ALG-SPRING-2008
  - [x] SRC-UCSD-ALG-SPRING-2009
  - [x] SRC-UCSD-ALG-SPRING-2011
  - [x] SRC-UCSD-ALG-SPRING-2012
  - [x] SRC-UCSD-ALG-SPRING-2013
  - [x] SRC-UCSD-ALG-SPRING-2014
  - [x] SRC-UCSD-ALG-SPRING-2015
  - [x] SRC-UCSD-ALG-SPRING-2016
  - [x] SRC-UCSD-ALG-SPRING-2017
  - [x] SRC-UCSD-ALG-SPRING-2018
  - [x] SRC-UCSD-ALG-SPRING-2019
  - [x] SRC-UCSD-ALG-SPRING-2020
  - [x] SRC-UCSD-ALG-SPRING-2021
  - [x] SRC-UCSD-ALG-SPRING-2022
  - [x] SRC-UCSD-ALG-SPRING-2023
  - [x] SRC-UCSD-ALG-SPRING-2024
  - [x] SRC-UCSD-ALG-SPRING-2025
  - [x] SRC-UCSD-ALG-SPRING-2026
  - [x] SRC-UCSD-APALG-FALL-2004
  - [x] SRC-UCSD-APALG-FALL-2006
  - [x] SRC-UCSD-APALG-FALL-2007
  - [x] SRC-UCSD-APALG-FALL-2011
  - [x] SRC-UCSD-APALG-FALL-2017
  - [x] SRC-UCSD-APALG-FALL-2018
  - [x] SRC-UCSD-APALG-FALL-2020
  - [x] SRC-UCSD-APALG-FALL-2021
  - [x] SRC-UCSD-APALG-FALL-2022
  - [x] SRC-UCSD-APALG-FALL-2023
  - [x] SRC-UCSD-APALG-FALL-2024
  - [x] SRC-UCSD-APALG-FALL-2025
  - [x] SRC-UCSD-APALG-SPRING-2004
  - [x] SRC-UCSD-APALG-SPRING-2005
  - [x] SRC-UCSD-APALG-SPRING-2006
  - [x] SRC-UCSD-APALG-SPRING-2007
  - [x] SRC-UCSD-APALG-SPRING-2008
  - [x] SRC-UCSD-APALG-SPRING-2011
  - [x] SRC-UCSD-APALG-SPRING-2013
  - [x] SRC-UCSD-APALG-SPRING-2015
  - [x] SRC-UCSD-APALG-SPRING-2017
  - [x] SRC-UCSD-APALG-SPRING-2018
  - [x] SRC-UCSD-APALG-SPRING-2019
  - [x] SRC-UCSD-APALG-SPRING-2020
  - [x] SRC-UCSD-APALG-SPRING-2021
  - [x] SRC-UCSD-APALG-SPRING-2022
  - [x] SRC-UCSD-APALG-SPRING-2023
  - [x] SRC-UCSD-APALG-SPRING-2024
  - [x] SRC-UCSD-APALG-SPRING-2026
  - [x] SRC-UCSD-CA-FALL-2005
  - [x] SRC-UCSD-CA-FALL-2006
  - [x] SRC-UCSD-CA-FALL-2007
  - [x] SRC-UCSD-CA-FALL-2008
  - [x] SRC-UCSD-CA-FALL-2009
  - [x] SRC-UCSD-CA-FALL-2010
  - [x] SRC-UCSD-CA-FALL-2011
  - [x] SRC-UCSD-CA-FALL-2013
  - [x] SRC-UCSD-CA-FALL-2015
  - [x] SRC-UCSD-CA-FALL-2016
  - [x] SRC-UCSD-CA-FALL-2017
  - [x] SRC-UCSD-CA-FALL-2019
  - [x] SRC-UCSD-CA-FALL-2020
  - [x] SRC-UCSD-CA-FALL-2021
  - [x] SRC-UCSD-CA-FALL-2022
  - [x] SRC-UCSD-CA-FALL-2023
  - [x] SRC-UCSD-CA-FALL-2024
  - [x] SRC-UCSD-CA-FALL-2025
  - [x] SRC-UCSD-CA-SPRING-2004
  - [x] SRC-UCSD-CA-SPRING-2005
  - [x] SRC-UCSD-CA-SPRING-2006
  - [x] SRC-UCSD-CA-SPRING-2007
  - [x] SRC-UCSD-CA-SPRING-2008
  - [x] SRC-UCSD-CA-SPRING-2009
  - [x] SRC-UCSD-CA-SPRING-2011
  - [x] SRC-UCSD-CA-SPRING-2012
  - [x] SRC-UCSD-CA-SPRING-2013
  - [x] SRC-UCSD-CA-SPRING-2015
  - [x] SRC-UCSD-CA-SPRING-2017
  - [x] SRC-UCSD-CA-SPRING-2018
  - [x] SRC-UCSD-CA-SPRING-2019
  - [x] SRC-UCSD-CA-SPRING-2020
  - [x] SRC-UCSD-CA-SPRING-2021
  - [x] SRC-UCSD-CA-SPRING-2022
  - [x] SRC-UCSD-CA-SPRING-2023
  - [x] SRC-UCSD-CA-SPRING-2024
  - [x] SRC-UCSD-CA-SPRING-2025
  - [x] SRC-UCSD-CA-SPRING-2026
  - [x] SRC-UCSD-RA-FALL-2004
  - [x] SRC-UCSD-RA-FALL-2005
  - [x] SRC-UCSD-RA-FALL-2006
  - [x] SRC-UCSD-RA-FALL-2007
  - [x] SRC-UCSD-RA-FALL-2009
  - [x] SRC-UCSD-RA-FALL-2010
  - [x] SRC-UCSD-RA-FALL-2011
  - [x] SRC-UCSD-RA-FALL-2016
  - [x] SRC-UCSD-RA-FALL-2017
  - [x] SRC-UCSD-RA-FALL-2018
  - [x] SRC-UCSD-RA-FALL-2020
  - [x] SRC-UCSD-RA-FALL-2021
  - [x] SRC-UCSD-RA-FALL-2022
  - [x] SRC-UCSD-RA-FALL-2023
  - [x] SRC-UCSD-RA-FALL-2024
  - [x] SRC-UCSD-RA-FALL-2025
  - [x] SRC-UCSD-RA-SPRING-2004
  - [x] SRC-UCSD-RA-SPRING-2006
  - [x] SRC-UCSD-RA-SPRING-2007
  - [x] SRC-UCSD-RA-SPRING-2008
  - [x] SRC-UCSD-RA-SPRING-2009
  - [x] SRC-UCSD-RA-SPRING-2011
  - [x] SRC-UCSD-RA-SPRING-2013
  - [x] SRC-UCSD-RA-SPRING-2015
  - [x] SRC-UCSD-RA-SPRING-2016
  - [x] SRC-UCSD-RA-SPRING-2017
  - [x] SRC-UCSD-RA-SPRING-2018
  - [x] SRC-UCSD-RA-SPRING-2020
  - [x] SRC-UCSD-RA-SPRING-2021
  - [x] SRC-UCSD-RA-SPRING-2022
  - [x] SRC-UCSD-RA-SPRING-2023
  - [x] SRC-UCSD-RA-SPRING-2024
  - [x] SRC-UCSD-RA-SPRING-2025
  - [x] SRC-UCSD-RA-SPRING-2026
  - [x] SRC-UCSD-TOP-290QUALS
  - [x] SRC-UCSD-TOP-FALL-2002
  - [x] SRC-UCSD-TOP-FALL-2003
  - [x] SRC-UCSD-TOP-FALL-2004
  - [x] SRC-UCSD-TOP-FALL-2006
  - [x] SRC-UCSD-TOP-FALL-2007
  - [x] SRC-UCSD-TOP-FALL-2008
  - [x] SRC-UCSD-TOP-FALL-2009
  - [x] SRC-UCSD-TOP-FALL-2010
  - [x] SRC-UCSD-TOP-FALL-2017
  - [x] SRC-UCSD-TOP-FALL-2018
  - [x] SRC-UCSD-TOP-FALL-2019
  - [x] SRC-UCSD-TOP-FALL-2020
  - [x] SRC-UCSD-TOP-FALL-2021
  - [x] SRC-UCSD-TOP-FALL-2022
  - [x] SRC-UCSD-TOP-FALL-2023
  - [x] SRC-UCSD-TOP-FALL-2024
  - [x] SRC-UCSD-TOP-FALL-2025
  - [x] SRC-UCSD-TOP-JUSTIN
  - [x] SRC-UCSD-TOP-QUAL-FALL-2017
  - [x] SRC-UCSD-TOP-SPRING-2000
  - [x] SRC-UCSD-TOP-SPRING-2001
  - [x] SRC-UCSD-TOP-SPRING-2002
  - [x] SRC-UCSD-TOP-SPRING-2004
  - [x] SRC-UCSD-TOP-SPRING-2005
  - [x] SRC-UCSD-TOP-SPRING-2006
  - [x] SRC-UCSD-TOP-SPRING-2007
  - [x] SRC-UCSD-TOP-SPRING-2008
  - [x] SRC-UCSD-TOP-SPRING-2010
  - [x] SRC-UCSD-TOP-SPRING-2011
  - [x] SRC-UCSD-TOP-SPRING-2013
  - [x] SRC-UCSD-TOP-SPRING-2017
  - [x] SRC-UCSD-TOP-SPRING-2018
  - [x] SRC-UCSD-TOP-SPRING-2020
  - [x] SRC-UCSD-TOP-SPRING-2022
  - [x] SRC-UCSD-TOP-SPRING-2023
  - [x] SRC-UCSD-TOP-SPRING-2024
  - [x] SRC-UCSD-TOP-SPRING-2025
  - [x] SRC-UCSD-TOP-SPRING-2026
  - [x] SRC-UCSD-TOP-SUMMER-2015
  - [x] SRC-UGA-ALG-FALL-2012
  - [x] SRC-UGA-ALG-FALL-2013
  - [x] SRC-UGA-ALG-FALL-2014
  - [x] SRC-UGA-ALG-FALL-2015
  - [x] SRC-UGA-ALG-FALL-2016
  - [x] SRC-UGA-ALG-FALL-2017
  - [x] SRC-UGA-ALG-FALL-2018
  - [x] SRC-UGA-ALG-FALL-2019
  - [x] SRC-UGA-ALG-FALL-2020
  - [x] SRC-UGA-ALG-FALL-2021
  - [x] SRC-UGA-ALG-SPRING-2012
  - [x] SRC-UGA-ALG-SPRING-2013
  - [x] SRC-UGA-ALG-SPRING-2014
  - [x] SRC-UGA-ALG-SPRING-2015
  - [x] SRC-UGA-ALG-SPRING-2016
  - [x] SRC-UGA-ALG-SPRING-2017
  - [x] SRC-UGA-ALG-SPRING-2018
  - [x] SRC-UGA-ALG-SPRING-2019
  - [x] SRC-UGA-ALG-SPRING-2020
  - [x] SRC-UGA-ALG-SPRING-2021
  - [x] SRC-UGA-CA-COMPILATION
  - [x] SRC-UGA-CA-FALL-2009
  - [x] SRC-UGA-CA-FALL-2011
  - [x] SRC-UGA-CA-FALL-2015
  - [x] SRC-UGA-CA-FALL-2016
  - [x] SRC-UGA-CA-FALL-2017
  - [x] SRC-UGA-CA-FALL-2018
  - [x] SRC-UGA-CA-FALL-2019
  - [x] SRC-UGA-CA-FALL-2020
  - [x] SRC-UGA-CA-FALL-2021
  - [x] SRC-UGA-CA-SPRING-2009
  - [x] SRC-UGA-CA-SPRING-2011
  - [x] SRC-UGA-CA-SPRING-2014
  - [x] SRC-UGA-CA-SPRING-2015
  - [x] SRC-UGA-CA-SPRING-2017
  - [x] SRC-UGA-CA-SPRING-2018
  - [x] SRC-UGA-CA-SPRING-2019
  - [x] SRC-UGA-CA-SPRING-2020
  - [x] SRC-UGA-CA-SPRING-2021
  - [x] SRC-UGA-MATH8150-SPRING-2020-FINAL
  - [x] SRC-UGA-MATH8150-SPRING-2020-MIDTERM
  - [x] SRC-UGA-MATH8150-SPRING-2021-HW1
  - [x] SRC-UGA-MATH8150-SPRING-2021-HW2
  - [x] SRC-UGA-MATH8150-SPRING-2021-HW3
  - [x] SRC-UGA-MATH8155-STARTER-PROBLEMS
  - [x] SRC-UGA-MATH8210-FALL-2018-HW1
  - [x] SRC-UGA-MATH8210-FALL-2018-HW2
  - [x] SRC-UGA-MATH8210-FALL-2018-HW3
  - [x] SRC-UGA-MATH8210-FALL-2018-HW4
  - [x] SRC-UGA-MATH8230-SPRING-2019
  - [x] SRC-UGA-PRELIM-FALL-2002
  - [x] SRC-UGA-PRELIM-FALL-2003
  - [x] SRC-UGA-PRELIM-FALL-2004
  - [x] SRC-UGA-PRELIM-FALL-2005
  - [x] SRC-UGA-PRELIM-FALL-2006
  - [x] SRC-UGA-PRELIM-FALL-2007
  - [x] SRC-UGA-PRELIM-FALL-2008
  - [x] SRC-UGA-PRELIM-FALL-2009
  - [x] SRC-UGA-PRELIM-FALL-2010
  - [x] SRC-UGA-PRELIM-FALL-2011
  - [x] SRC-UGA-PRELIM-FALL-2012
  - [x] SRC-UGA-PRELIM-FALL-2013
  - [x] SRC-UGA-PRELIM-FALL-2014
  - [x] SRC-UGA-PRELIM-FALL-2015
  - [x] SRC-UGA-PRELIM-FALL-2016
  - [x] SRC-UGA-PRELIM-FALL-2017
  - [x] SRC-UGA-PRELIM-SPRING-2003
  - [x] SRC-UGA-PRELIM-SPRING-2004
  - [x] SRC-UGA-PRELIM-SPRING-2005
  - [x] SRC-UGA-PRELIM-SPRING-2006
  - [x] SRC-UGA-PRELIM-SPRING-2007
  - [x] SRC-UGA-PRELIM-SPRING-2008
  - [x] SRC-UGA-PRELIM-SPRING-2009
  - [x] SRC-UGA-RA-FALL-2014
  - [x] SRC-UGA-RA-FALL-2015
  - [x] SRC-UGA-RA-FALL-2016
  - [x] SRC-UGA-RA-FALL-2017
  - [x] SRC-UGA-RA-FALL-2018
  - [x] SRC-UGA-RA-FALL-2019
  - [x] SRC-UGA-RA-FALL-2020
  - [x] SRC-UGA-RA-FALL-2021
  - [x] SRC-UGA-RA-SPRING-2005
  - [x] SRC-UGA-RA-SPRING-2006
  - [x] SRC-UGA-RA-SPRING-2007
  - [x] SRC-UGA-RA-SPRING-2008
  - [x] SRC-UGA-RA-SPRING-2009
  - [x] SRC-UGA-RA-SPRING-2010
  - [x] SRC-UGA-RA-SPRING-2011
  - [x] SRC-UGA-RA-SPRING-2012
  - [x] SRC-UGA-RA-SPRING-2014
  - [x] SRC-UGA-RA-SPRING-2015
  - [x] SRC-UGA-RA-SPRING-2016
  - [x] SRC-UGA-RA-SPRING-2017
  - [x] SRC-UGA-RA-SPRING-2018
  - [x] SRC-UGA-RA-SPRING-2019
  - [x] SRC-UGA-RA-SPRING-2020
  - [x] SRC-UGA-RA-SPRING-2021
  - [x] SRC-UGA-TOP-FALL-2004
  - [x] SRC-UGA-TOP-FALL-2005
  - [x] SRC-UGA-TOP-FALL-2006
  - [x] SRC-UGA-TOP-FALL-2007
  - [x] SRC-UGA-TOP-FALL-2009
  - [x] SRC-UGA-TOP-FALL-2010
  - [x] SRC-UGA-TOP-FALL-2011
  - [x] SRC-UGA-TOP-FALL-2012
  - [x] SRC-UGA-TOP-FALL-2013
  - [x] SRC-UGA-TOP-FALL-2014
  - [x] SRC-UGA-TOP-FALL-2015
  - [x] SRC-UGA-TOP-FALL-2016
  - [x] SRC-UGA-TOP-FALL-2017
  - [x] SRC-UGA-TOP-FALL-2018
  - [x] SRC-UGA-TOP-SPRING-2005
  - [x] SRC-UGA-TOP-SPRING-2006
  - [x] SRC-UGA-TOP-SPRING-2007
  - [x] SRC-UGA-TOP-SPRING-2008
  - [x] SRC-UGA-TOP-SPRING-2009
  - [x] SRC-UGA-TOP-SPRING-2010
  - [x] SRC-UGA-TOP-SPRING-2011
  - [x] SRC-UGA-TOP-SPRING-2012
  - [x] SRC-UGA-TOP-SPRING-2013
  - [x] SRC-UGA-TOP-SPRING-2014
  - [x] SRC-UGA-TOP-SPRING-2015
  - [x] SRC-UGA-TOP-SPRING-2016
  - [x] SRC-UGA-TOP-SPRING-2017
  - [x] SRC-UGA-TOP-SPRING-2018
  - [x] SRC-UGA-TOP-SPRING-2019
  - [x] SRC-UGA-TOP-SPRING-2021
  - [x] SRC-UMN-COMPLEX-PRELIM-BAHRAN-2013
  - [x] SRC-UNL-MATH871-FALL-2013-PROBLEM-SETS
  - [x] SRC-UNL-MATH872-SPRING-2014-PROBLEM-SETS
  - [x] SRC-UNL-QUAL-850-871-JANUARY-2006
  - [x] SRC-UNL-QUAL-850-871-JANUARY-2008
  - [x] SRC-UNL-QUAL-852-871-JUNE-2007
  - [x] SRC-UNL-QUAL-852-970-JANUARY-2006
  - [x] SRC-UNL-QUAL-970-953-JANUARY-2004
  - [x] SRC-UNL-QUAL-JUNE-2004-970-852
  - [x] SRC-UNL-RA-SPRING-2019
  - [x] SRC-UNL-RA-SUMMER-2016
  - [x] SRC-UNL-RA-SUMMER-2018
  - [x] SRC-UNSORTED-ALGEBRA
  - [x] SRC-UNSORTED-COMPLEX-ANALYSIS
  - [x] SRC-UNSORTED-PRELIM
  - [x] SRC-UNSORTED-REAL-ANALYSIS
  - [x] SRC-UNSORTED-TOPOLOGY
  - [ ] SRC-UO-TOP-FALL-2019
  - [ ] SRC-UT-M392C-CONTACT-TOPOLOGY-FALL-2017
  - [ ] SRC-UW-ALG-2005
  - [ ] SRC-UW-ALG-2006
  - [ ] SRC-UW-ALG-2007
  - [ ] SRC-UW-ALG-2008
  - [ ] SRC-UW-ALG-2009
  - [ ] SRC-UW-ALG-2010
  - [ ] SRC-UW-ALG-2011
  - [ ] SRC-UW-ALG-2012
  - [ ] SRC-UW-ALG-2013
  - [ ] SRC-UW-ALG-2014
  - [ ] SRC-UW-ALG-2015
  - [ ] SRC-UW-ALG-2016
  - [ ] SRC-UW-ALG-2017
  - [ ] SRC-UW-ALG-2018
  - [ ] SRC-UW-ALGEBRA-2005-2018
  - [ ] SRC-VAKIL-RISINGSEA
  - [ ] SRC-WESLEYAN-ANALYSIS-2003-2007
  - [ ] SRC-WESLEYAN-ANALYSIS-2008-2013
  - [ ] SRC-WESLEYAN-ANALYSIS-2014-2016
  - [ ] SRC-WESLEYAN-TOPOLOGY-2003-2005
  - [ ] SRC-WESLEYAN-TOPOLOGY-2006-2014
  Wiki pages:
  - [x] wiki/algebra/counterexamples.md
  - [x] wiki/algebra/fields/extensions.md
  - [x] wiki/algebra/fields/finite-fields.md
  - [x] wiki/algebra/fields/index.md
  - [x] wiki/algebra/fields/polynomials.md
  - [x] wiki/algebra/fields/review-sheet-1.md
  - [x] wiki/algebra/fields/separability.md
  - [x] wiki/algebra/fields/splitting-and-normal.md
  - [x] wiki/algebra/galois-theory/compute-this-galois-group.md
  - [x] wiki/algebra/galois-theory/cyclotomic-and-radical-extensions.md
  - [x] wiki/algebra/galois-theory/index.md
  - [x] wiki/algebra/galois-theory/the-correspondence.md
  - [x] wiki/algebra/galois-theory/worked-examples.md
  - [x] wiki/algebra/group-actions/index.md
  - [x] wiki/algebra/group-actions/orbit-stabilizer.md
  - [x] wiki/algebra/group-actions/show-g-is-not-simple.md
  - [x] wiki/algebra/group-actions/sylow.md
  - [x] wiki/algebra/group-actions/the-class-equation.md
  - [x] wiki/algebra/groups/basics.md
  - [x] wiki/algebra/groups/characteristic-subgroups.md
  - [x] wiki/algebra/groups/groups-of-small-order.md
  - [x] wiki/algebra/groups/index.md
  - [x] wiki/algebra/groups/is-this-group-abelian.md
  - [x] wiki/algebra/groups/notation.md
  - [x] wiki/algebra/groups/quotients-and-products.md
  - [x] wiki/algebra/groups/series-and-solvability.md
  - [x] wiki/algebra/groups/the-standard-families.md
  - [x] wiki/algebra/index.md
  - [x] wiki/algebra/linear-algebra/determinants-and-eigenvalues.md
  - [x] wiki/algebra/linear-algebra/find-the-canonical-form.md
  - [x] wiki/algebra/linear-algebra/index.md
  - [x] wiki/algebra/linear-algebra/jordan-canonical-form.md
  - [x] wiki/algebra/linear-algebra/matrix-counterexamples.md
  - [x] wiki/algebra/linear-algebra/minimal-and-characteristic-polynomials.md
  - [x] wiki/algebra/linear-algebra/rational-canonical-form.md
  - [x] wiki/algebra/linear-algebra/smith-normal-form.md
  - [x] wiki/algebra/linear-algebra/the-spectral-theorem.md
  - [x] wiki/algebra/linear-algebra/undergrad-review.md
  - [x] wiki/algebra/modules/classify-this-module.md
  - [x] wiki/algebra/modules/exact-sequences.md
  - [x] wiki/algebra/modules/free-and-projective.md
  - [x] wiki/algebra/modules/index.md
  - [x] wiki/algebra/modules/over-a-pid.md
  - [x] wiki/algebra/representations/characters.md
  - [x] wiki/algebra/representations/index.md
  - [x] wiki/algebra/representations/maschke-and-schur.md
  - [x] wiki/algebra/resources/books-notes.md
  - [x] wiki/algebra/resources/external.md
  - [x] wiki/algebra/resources/fields.md
  - [x] wiki/algebra/resources/groups.md
  - [x] wiki/algebra/resources/index.md
  - [x] wiki/algebra/resources/modules.md
  - [x] wiki/algebra/resources/problems.md
  - [x] wiki/algebra/resources/representations.md
  - [x] wiki/algebra/resources/rings-and-ideals.md
  - [x] wiki/algebra/resources/solutions-algebra.md
  - [x] wiki/algebra/resources/syllabus.md
  - [x] wiki/algebra/review.md
  - [x] wiki/algebra/rings-and-ideals/commutative-algebra.md
  - [x] wiki/algebra/rings-and-ideals/domains-and-factorization.md
  - [x] wiki/algebra/rings-and-ideals/ideals-and-quotients.md
  - [x] wiki/algebra/rings-and-ideals/index.md
  - [x] wiki/algebra/rings-and-ideals/number-theory.md
  - [x] wiki/algebra/rings-and-ideals/polynomial-rings.md
  - [x] wiki/algebra/rings-and-ideals/solutions.md
  - [x] wiki/algebra/rings-and-ideals/which-kind-of-ring.md
  - [x] wiki/algebra/workshops/algebra-week-1-groups-warmup.md
  - [x] wiki/algebra/workshops/algebra-week-2-finite-group-theory.md
  - [x] wiki/algebra/workshops/algebra-week-3-sylow-theory.md
  - [x] wiki/algebra/workshops/algebra-week-4-rings.md
  - [x] wiki/algebra/workshops/algebra-week-n-1-linear-algebra.md
  - [x] wiki/algebra/workshops/algebra-week-n-rep-theory.md
  - [x] wiki/algebra/workshops/index.md
  - [x] wiki/algebraic-geometry/cohomology/computing-cohomology.md
  - [x] wiki/algebraic-geometry/cohomology/derived-functors-and-vanishing.md
  - [x] wiki/algebraic-geometry/cohomology/families.md
  - [x] wiki/algebraic-geometry/cohomology/index.md
  - [x] wiki/algebraic-geometry/cohomology/projective-schemes.md
  - [x] wiki/algebraic-geometry/cohomology/vanishing-and-duality.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/blowups-and-the-classification-of-surfaces.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/curves-in-projective-space.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/elliptic-curves-over-c.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/elliptic-curves.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/embeddings-and-jacobians.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/genus.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/index.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/intersection-theory-on-surfaces.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/moduli-of-curves.md
  - [x] wiki/algebraic-geometry/curves-and-surfaces/special-divisors-and-the-canonical-map.md
  - [x] wiki/algebraic-geometry/divisors/index.md
  - [x] wiki/algebraic-geometry/divisors/line-bundles-and-linear-systems.md
  - [x] wiki/algebraic-geometry/divisors/positivity.md
  - [x] wiki/algebraic-geometry/divisors/weil-and-cartier.md
  - [x] wiki/algebraic-geometry/index.md
  - [x] wiki/algebraic-geometry/morphisms/classes-of-morphism.md
  - [x] wiki/algebraic-geometry/morphisms/fibres-and-images.md
  - [x] wiki/algebraic-geometry/morphisms/finite-and-flat.md
  - [x] wiki/algebraic-geometry/morphisms/index.md
  - [x] wiki/algebraic-geometry/morphisms/inseparable-morphisms-and-luroth.md
  - [x] wiki/algebraic-geometry/morphisms/separated-and-proper.md
  - [x] wiki/algebraic-geometry/morphisms/smooth-unramified-etale.md
  - [x] wiki/algebraic-geometry/resources.md
  - [x] wiki/algebraic-geometry/schemes/fibre-products-and-base-change.md
  - [x] wiki/algebraic-geometry/schemes/index.md
  - [x] wiki/algebraic-geometry/schemes/proj-and-gluing.md
  - [x] wiki/algebraic-geometry/schemes/properties-from-the-ring.md
  - [x] wiki/algebraic-geometry/schemes/subschemes-and-points.md
  - [x] wiki/algebraic-geometry/schemes/what-is-a-scheme.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/differentials.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/index.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/line-bundles.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/operations.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/projective-sheaves.md
  - [x] wiki/algebraic-geometry/sheaves-of-modules/quasicoherence.md
  - [x] wiki/algebraic-geometry/sheaves/index.md
  - [x] wiki/algebraic-geometry/sheaves/stalks-and-exactness.md
  - [x] wiki/algebraic-geometry/sheaves/the-sheaf-condition.md
  - [x] wiki/algebraic-geometry/stacks-and-moduli/functors-and-topologies.md
  - [x] wiki/algebraic-geometry/stacks-and-moduli/index.md
  - [x] wiki/algebraic-geometry/stacks-and-moduli/spaces-and-stacks.md
  - [x] wiki/algebraic-geometry/syllabus.md
  - [x] wiki/algebraic-geometry/toric/affine-computations.md
  - [x] wiki/algebraic-geometry/toric/criteria.md
  - [x] wiki/algebraic-geometry/toric/index.md
  - [x] wiki/algebraic-geometry/toric/polytopes-and-divisors.md
  - [x] wiki/algebraic-geometry/toric/surfaces-and-morphisms.md
  - [x] wiki/algebraic-geometry/toric/the-dictionary.md
  - [x] wiki/algebraic-geometry/varieties/affine-or-projective.md
  - [x] wiki/algebraic-geometry/varieties/blowups.md
  - [x] wiki/algebraic-geometry/varieties/canonical-class.md
  - [x] wiki/algebraic-geometry/varieties/dimension-and-degree.md
  - [x] wiki/algebraic-geometry/varieties/index.md
  - [x] wiki/algebraic-geometry/varieties/regular-functions.md
  - [x] wiki/algebraic-geometry/varieties/smooth-and-singular.md
  - [x] wiki/algebraic-geometry/varieties/the-dictionary.md
  - [x] wiki/applied-algebra/grobner-bases/index.md
  - [x] wiki/applied-algebra/index.md
  - [x] wiki/applied-algebra/invariant-theory/index.md
  - [x] wiki/applied-algebra/matrix-analysis/index.md
  - [x] wiki/applied-algebra/representation-theory/index.md
  - [x] wiki/applied-algebra/resources/index.md
  - [x] wiki/applied-algebra/symmetric-functions/index.md
  - [x] wiki/archives/card-archives.md
  - [x] wiki/archives/further-studying.md
  - [x] wiki/archives/graduate-topics.md
  - [x] wiki/archives/index.md
  - [x] wiki/archives/qual-workshop-index.md
  - [x] wiki/archives/solution-compendia.md
  - [x] wiki/archives/topics.md
  - [x] wiki/complex-analysis/appendices/appendix-fta-proofs.md
  - [x] wiki/complex-analysis/appendices/appendix-unsorted.md
  - [x] wiki/complex-analysis/appendices/gauss-lucas-theorem.md
  - [x] wiki/complex-analysis/appendices/index.md
  - [x] wiki/complex-analysis/appendices/pdes.md
  - [x] wiki/complex-analysis/appendices/special-functions.md
  - [x] wiki/complex-analysis/basics/analytic-nt.md
  - [x] wiki/complex-analysis/basics/calculus-preliminaries.md
  - [x] wiki/complex-analysis/basics/complex-arithmetic.md
  - [x] wiki/complex-analysis/basics/index.md
  - [x] wiki/complex-analysis/basics/precalculus.md
  - [x] wiki/complex-analysis/basics/series-reference.md
  - [x] wiki/complex-analysis/basics/tips-techs.md
  - [x] wiki/complex-analysis/cauchy-theory/cauchy-estimates-and-liouville.md
  - [x] wiki/complex-analysis/cauchy-theory/cauchys-theorem.md
  - [x] wiki/complex-analysis/cauchy-theory/index.md
  - [x] wiki/complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping.md
  - [x] wiki/complex-analysis/cauchy-theory/morera-and-converses.md
  - [x] wiki/complex-analysis/cauchy-theory/schwarz-reflection.md
  - [x] wiki/complex-analysis/cauchy-theory/the-identity-principle.md
  - [x] wiki/complex-analysis/cauchy-theory/the-integral-formula.md
  - [x] wiki/complex-analysis/cauchy-theory/theorems-that-give-a-constant.md
  - [x] wiki/complex-analysis/conformal-maps/blaschke-factors-and-automorphisms.md
  - [x] wiki/complex-analysis/conformal-maps/build-me-a-map.md
  - [x] wiki/complex-analysis/conformal-maps/index.md
  - [x] wiki/complex-analysis/conformal-maps/mobius-transformations.md
  - [x] wiki/complex-analysis/conformal-maps/normal-families-and-montel.md
  - [x] wiki/complex-analysis/conformal-maps/the-riemann-mapping-theorem.md
  - [x] wiki/complex-analysis/conformal-maps/the-schwarz-lemma.md
  - [x] wiki/complex-analysis/counterexamples.md
  - [x] wiki/complex-analysis/counting-zeros/how-many-zeros-in-this-region.md
  - [x] wiki/complex-analysis/counting-zeros/hurwitz.md
  - [x] wiki/complex-analysis/counting-zeros/index.md
  - [x] wiki/complex-analysis/counting-zeros/rouches-theorem.md
  - [x] wiki/complex-analysis/counting-zeros/the-argument-principle.md
  - [x] wiki/complex-analysis/holomorphic-functions/complex-arithmetic-and-log.md
  - [x] wiki/complex-analysis/holomorphic-functions/harmonic-functions.md
  - [x] wiki/complex-analysis/holomorphic-functions/index.md
  - [x] wiki/complex-analysis/holomorphic-functions/is-it-holomorphic.md
  - [x] wiki/complex-analysis/holomorphic-functions/power-series.md
  - [x] wiki/complex-analysis/holomorphic-functions/the-cauchy-riemann-equations.md
  - [x] wiki/complex-analysis/index.md
  - [x] wiki/complex-analysis/residues-and-contours/arc-estimates.md
  - [x] wiki/complex-analysis/residues-and-contours/computing-residues.md
  - [x] wiki/complex-analysis/residues-and-contours/index.md
  - [x] wiki/complex-analysis/residues-and-contours/real-integrals-by-residues.md
  - [x] wiki/complex-analysis/residues-and-contours/the-residue-theorem.md
  - [x] wiki/complex-analysis/residues-and-contours/which-contour-do-i-close.md
  - [x] wiki/complex-analysis/resources/books-notes.md
  - [x] wiki/complex-analysis/resources/index.md
  - [x] wiki/complex-analysis/resources/problems.md
  - [x] wiki/complex-analysis/resources/solutions.md
  - [x] wiki/complex-analysis/resources/study-schedule-and-topics.md
  - [x] wiki/complex-analysis/review.md
  - [x] wiki/complex-analysis/singularities/casorati-weierstrass-and-picard.md
  - [x] wiki/complex-analysis/singularities/classifying-a-singularity.md
  - [x] wiki/complex-analysis/singularities/index.md
  - [x] wiki/complex-analysis/singularities/laurent-series.md
  - [x] wiki/complex-analysis/singularities/meromorphic-functions.md
  - [x] wiki/complex-analysis/singularities/removable-poles-essential.md
  - [x] wiki/complex-analysis/standard-integrals.md
  - [x] wiki/complex-analysis/workshops/complex-week-1-preliminaries.md
  - [x] wiki/complex-analysis/workshops/complex-week-2-cauchy.md
  - [x] wiki/complex-analysis/workshops/index.md
  - [x] wiki/index.md
  - [x] wiki/prelim/counterexamples.md
  - [x] wiki/prelim/index.md
  - [x] wiki/prelim/problems/berkeley-prelims.md
  - [x] wiki/prelim/problems/index.md
  - [x] wiki/prelim/problems/integral-practice.md
  - [x] wiki/prelim/problems/ucla-prelims.md
  - [x] wiki/prelim/resources/index.md
  - [x] wiki/prelim/resources/problems.md
  - [x] wiki/prelim/resources/references.md
  - [x] wiki/prelim/resources/solutions.md
  - [x] wiki/prelim/resources/topics.md
  - [x] wiki/prelim/useful-tricks.md
  - [x] wiki/prelim/which-technique.md
  - [x] wiki/prelim/worked-exams/all.md
  - [x] wiki/prelim/worked-exams/fall-2014.md
  - [x] wiki/prelim/worked-exams/fall-2015.md
  - [x] wiki/prelim/worked-exams/fall-2016.md
  - [x] wiki/prelim/worked-exams/fall-2017.md
  - [x] wiki/prelim/worked-exams/index.md
  - [x] wiki/real-analysis/appendices/appendix-inequalities.md
  - [x] wiki/real-analysis/appendices/functional-analysis.md
  - [x] wiki/real-analysis/appendices/index.md
  - [x] wiki/real-analysis/appendices/undergrad-appendix.md
  - [x] wiki/real-analysis/counterexamples-undergraduate.md
  - [x] wiki/real-analysis/counterexamples.md
  - [x] wiki/real-analysis/fourier/convolution.md
  - [x] wiki/real-analysis/fourier/index.md
  - [x] wiki/real-analysis/fourier/the-transform.md
  - [x] wiki/real-analysis/fubini-tonelli/index.md
  - [x] wiki/real-analysis/fubini-tonelli/statements.md
  - [x] wiki/real-analysis/fubini-tonelli/which-one-applies.md
  - [x] wiki/real-analysis/functional-analysis/banach-and-hilbert.md
  - [x] wiki/real-analysis/functional-analysis/index.md
  - [x] wiki/real-analysis/functional-analysis/operators.md
  - [x] wiki/real-analysis/functional-analysis/which-big-theorem.md
  - [x] wiki/real-analysis/index.md
  - [x] wiki/real-analysis/inequalities.md
  - [x] wiki/real-analysis/integration/construction.md
  - [x] wiki/real-analysis/integration/index.md
  - [x] wiki/real-analysis/integration/l1.md
  - [x] wiki/real-analysis/integration/the-convergence-theorems.md
  - [x] wiki/real-analysis/integration/which-convergence-theorem.md
  - [x] wiki/real-analysis/lp-spaces/index.md
  - [x] wiki/real-analysis/lp-spaces/the-spaces.md
  - [x] wiki/real-analysis/lp-spaces/which-inequality.md
  - [x] wiki/real-analysis/measure/index.md
  - [x] wiki/real-analysis/measure/is-it-measurable.md
  - [x] wiki/real-analysis/measure/littlewood-principles-notes.md
  - [x] wiki/real-analysis/measure/littlewoods-principles.md
  - [x] wiki/real-analysis/measure/outer-measure.md
  - [x] wiki/real-analysis/resources/books-notes.md
  - [x] wiki/real-analysis/resources/extra-questions.md
  - [x] wiki/real-analysis/resources/index.md
  - [x] wiki/real-analysis/resources/preface.md
  - [x] wiki/real-analysis/resources/problems.md
  - [x] wiki/real-analysis/resources/solutions.md
  - [x] wiki/real-analysis/resources/topics.md
  - [x] wiki/real-analysis/review.md
  - [x] wiki/real-analysis/undergraduate/advice.md
  - [x] wiki/real-analysis/undergraduate/commuting-limits.md
  - [x] wiki/real-analysis/undergraduate/continuity.md
  - [x] wiki/real-analysis/undergraduate/definitions.md
  - [x] wiki/real-analysis/undergraduate/differentiability.md
  - [x] wiki/real-analysis/undergraduate/index.md
  - [x] wiki/real-analysis/undergraduate/notation.md
  - [x] wiki/real-analysis/undergraduate/riemann-integrability.md
  - [x] wiki/real-analysis/undergraduate/sequences-and-series.md
  - [x] wiki/real-analysis/undergraduate/sets-and-compactness.md
  - [x] wiki/real-analysis/undergraduate/theorem-list.md
  - [x] wiki/real-analysis/workshops/index.md
  - [x] wiki/real-analysis/workshops/real-week-1-preliminaries.md
  - [x] wiki/real-analysis/workshops/real-week-2-measure-theory.md
  - [x] wiki/topology/appendices/appendix.md
  - [x] wiki/topology/appendices/at-course-notes.md
  - [x] wiki/topology/appendices/index.md
  - [x] wiki/topology/counterexamples.md
  - [x] wiki/topology/covering-spaces/covering-spaces.md
  - [x] wiki/topology/covering-spaces/index.md
  - [x] wiki/topology/cw-complexes/cw-complexes.md
  - [x] wiki/topology/cw-complexes/index.md
  - [x] wiki/topology/degree/fixed-points-and-degree.md
  - [x] wiki/topology/degree/index.md
  - [x] wiki/topology/fundamental-group/compute-pi-1.md
  - [x] wiki/topology/fundamental-group/index.md
  - [x] wiki/topology/fundamental-group/theorems.md
  - [x] wiki/topology/homology/compute-h-star.md
  - [x] wiki/topology/homology/exercises.md
  - [x] wiki/topology/homology/homological-algebra.md
  - [x] wiki/topology/homology/homology.md
  - [x] wiki/topology/homology/index.md
  - [x] wiki/topology/index.md
  - [x] wiki/topology/point-set/definitions.md
  - [x] wiki/topology/point-set/examples.md
  - [x] wiki/topology/point-set/index.md
  - [x] wiki/topology/point-set/notation-and-background.md
  - [x] wiki/topology/point-set/point-set.md
  - [x] wiki/topology/resources/books-notes.md
  - [x] wiki/topology/resources/index.md
  - [x] wiki/topology/resources/problems.md
  - [x] wiki/topology/resources/solutions.md
  - [x] wiki/topology/resources/topics.md
  - [x] wiki/topology/review.md
  - [x] wiki/topology/surfaces/index.md
  - [x] wiki/topology/surfaces/surfaces-and-manifolds.md
  - [x] wiki/topology/the-standard-spaces.md
  - [x] wiki/topology/workshops/index.md
  - [x] wiki/topology/workshops/topology-week-1-preliminaries.md
  Site surfaces:
  - [x] index, sources, problems, bibliography, search

  Renderer and site nodes (owner `tools/qualc`, `site/`):
  - **`ad-citeproc`**. **Needs:** none. Citations in transcluded card bodies render as raw
    `[@key]`. **Acceptance:** no deployed page shows a literal `[@`. **Closed.**
  - **`ad-tikzcd`**. **Needs:** none. `tikzcd` blocks vanish on transclusion (D-KRKV7,
    T-SKJB2, E-B4ZSQ). **Acceptance:** every card diagram renders wherever the card appears.
  - **`ad-fancy-lists`**. **Needs:** none. A proof step opening with `(a)` splits into a
    bare number and a list. **Acceptance:** such steps render as one numbered claim. **Closed.**
  - **`ad-smart-titles`**. **Needs:** none. `--` and `$…$` reach titles, prompts, link
    text and `<title>`. **Acceptance:** dashes typeset; tab titles carry no TeX. **Closed.**
  - **`ad-bare-id-links`**. **Needs:** none. 148 wikilinks display a bare card id.
    **Acceptance:** link text is the card title or authored text. **Closed.**
  - **`ad-collection-pages`**. **Needs:** none. Drop cap splits the count; "1 problems.";
    derived "Problem N" locators; transcluded collections render empty (workshop packets).
    **Acceptance:** each corrected on the deployed pages. **Closed.**
  - **`ad-site-strings`**. **Needs:** none. Unmatched browser prefilter widens to all rows;
    `sourced` compatibility filter; Sources/Exams naming; area label spellings; Pagefind
    excerpts include page facts; "Choose topic" over areas; home contents list.
    **Acceptance:** each corrected on the deployed pages. **Closed.**

  Round 2 (revision `848f40677`) injected:
  - **`ad2-renderer`**. **Needs:** none. `--` in wikilink text, block qualifiers and slogans;
    citation style dropped locators such as `Section 10.1`. **Closed.**
  - **`ad2-algebra-content`**. **Needs:** none. CARD-04: PR-TAPZF/FF-UYMWY; FD-XT6HD/PR-TI6YA;
    PR-QDRB4/PR-3TYBE; PR-E4T3S/resolvent-cubic remark; T-V7JRG/FT-PUVIQ; P-UZDCX/T-NGBVC;
    P-ZYHXO/FD-3GZPO; C-BOM4E/PR-OFBRQ; FF-2AKVH/FF-HAMDC; separability cluster PR-TLBPS,
    PR-ENHVC, FD-6WSIA, C-C2GYX, E-6OUJV. which-kind-of-ring claims 3 and 3 are nonassociate.
    PR-DLPTR restates D-LIEMF. Page restatements: finite-fields, fields/polynomials,
    commutative-algebra, which-kind-of-ring, maschke-and-schur. **Acceptance:** each read and repaired.
    **Closed.** P-UZDCX stays distinct from T-NGBVC: it also asks why a finitely generated
    algebraic extension is finite.
  - **`ad2-real-analysis-content`**. **Needs:** none. PR-WUZSG uniform-convergence criterion
    needs "for all sufficiently large n"; the-convergence-theorems "on $L^1$" should read
    "on $\RR$"; P-RAF23C, P-RAF23F, P-RAF23G proof notation, part labels and step references;
    P-4EOE5 doubled arrow and typed step citations; CARD-04 groups on measure, integration and
    $L^p$ (T-BFOJT/FT-4ED3Q/PR-JX4YU, FT-O4DRR/FF-LA4J2, T-OTR5M/FR-CSUMF/FF-GNU7E/P-QZT5B,
    FF-UW3C7/FE-YOIJM, T-CGFCU/FT-XIVPL, T-5K3IO/FT-5G4Y3, T-IJQQG/FT-LCR5P, T-LDJNS/FT-P5UNP,
    T-MN6WQ/FS-BM2PV/PR-EHIXY/FR-KEWV2/PR-NKZBT/PR-YJJSY, D-R4VKE/FD-Q3XHG,
    FF-C7GY4/FF-LMANJ/PR-6OHTJ, T-RIY2P/FT-BV2AU/FF-FSDJP/PR-4OXGZ, PR-HFYSO/FR-6AHGM,
    T-X7XZX/FT-H6AWV, PR-V4MOK/PR-2CZUM, E-WXIRH/PR-TNFL4) and the PR-2JV43 repeated remark;
    CARD-04 groups on other pages (FF-AVBFU/FF-5EBCJ, PR-UJ64S/PR-LEDI3, FD-5I73B/FF-7JOOD,
    D-YZC3C/FD-ZTRHG/D-RA-WORKSHOP-D7-CONVERGENCE, FD-WN55Z/FF-HORGP, D-2MJRE/FF-HRUA3,
    D-5NODS/FD-JGBSF, D-PAEDW/FD-AI6XN/FF-JBCFQ, D-RPOGQ/FD-BBR6Q/FD-HGESN, FD-5T3HX/FF-NOX4C,
    D-3PVRB/FD-J5AFR, D-TS42Y/FF-4WIMZ, PR-JTFMW/C-44LL4, PR-ZI7M3/FT-NFMJW/T-5AALA,
    T-LDCZB/FF-UT5GL); workshop theorem cards T-RA-WORKSHOP-D5-4-2/T-OXNTU,
    T-RA-WORKSHOP-D4-3-3/T-O4UD3, T-RA-WORKSHOP-D7-6-2/FF-IAUQG, T-RA-WORKSHOP-D7-6-7/T-3QNBQ,
    T-RA-WORKSHOP-D7-6-1/C-3S4XS, T-RA-WORKSHOP-D5-4-3/T-2R7PC, T-RA-WORKSHOP-D7-6-5/FF-XZGIY;
    `STYLE-03`, `STYLE-04`, `STYLE-08` in P-ZCE6E, P-8RA35, P-4NYI7, P-4EOE5, T-W5SDY and the
    SRC-RA-WORKSHOP problem cards; real-analysis round-2 candidates (FS-5FKPD/FF-IAUQG,
    PR-DWOXP/FE-GN3CF, PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE, D-HHVPT/FD-ST7TD, P-7XPOK and
    P-PEND3 overlaps, real-week-2-measure-theory process text, P-OPH7A prose solution,
    "orthonormal" in FT-NFMJW and PR-ZI7M3, Arzelà–Ascoli codomain, T-ERNLN notation).
    **Acceptance:** each read and repaired. **Closed.** Every CARD-04 group was one
    statement and is merged into the surviving card named first; the workshop theorem cards
    merged into their pairs, and D-RA-WORKSHOP-D7-CONVERGENCE into D-IYDZU and D-YZC3C, with
    the series forms as remarks. T-RA-WORKSHOP-D7-6-7 stays as Stone--Weierstrass, which no
    other card states; Weierstrass approximation lives on T-3QNBQ. FS-5FKPD stays apart from
    FF-IAUQG: it is the strategy for showing a series converges uniformly and cites the
    $M$-test. P-7XPOK merged into E-MFCCS, E-EJN4Q, E-M3CGY, E-L3F4O and T-OTR5M.
  - **`ad2-topology-content`**. **Needs:** none. Citation-only `concept` blocks on about 80
    topology cards (D-EBNUE, D-IGUUS, …); FF-AE7ID/C-CT2NX merge; fundamental-group/theorems
    change-of-basepoint restatement; curves-in-projective-space opening and projection
    paragraphs; T-2YTCZ proof notation. **Acceptance:** each read and repaired.
    **Closed.** D-BUAYX, a second injective-map card, was merged into D-3ZBXG, and
    D-CNLBT, D-JW63I and D-K5MLW (orientation, local orientation, orientable) into D-6CI7D;
    the fundamental-class theorem stays on D-TS7TZ. D-QTJ7T and T-TUXBP (complex analysis) keep citation-only
    `concept` blocks.
  - **`ad2-style-03-corpus`**. **Needs:** none. Raw blackboard bold replaced by semantic macros,
    one per meaning, defined in the pandoc-config preamble. **Closed.** Codemods 579287fd3f,
    8176772bad and 2b05c0f015; the card check rejects any raw `\mathbb` or `\Bbb`.
    Bold vectors and points written `\mathbf` (P-GRECH3-04, P-AGH5415GENPOSITION) stay raw.
  - **`ad2-complex-analysis-content`**. **Needs:** none. The power-series Dirichlet's-test proof
    swaps the two sequences. CARD-04: PR-K57J6/E-TZJKN; E-6F2HU/E-THK2Z; PR-OOHUL/E-PAQPF;
    PR-Y36BS/D-E7A5W proposition/Cauchy–Riemann page remark; T-E76LX/P-Y5SS5; D-4CSPM/D-OMBQT;
    T-GROTS/T-SRY2V/C-7S2CO; PR-NZZ2C/E-EG3W7; T-77SHB/PR-FL6T7; PR-AQFRA/PR-PDYJC; T-DAETF/T-VM6MJ;
    E-TJ3WM/E-XQ4BA; T-W26VL/FF-4GUYL; D-MFPYG proposition/PR-ULJAJ; C-FVT4V/P-Z776N/E-I26BF/D-OHFRH
    proposition; T-MCB7V/T-4ALS2; E-ISFYB/E-C5QHZ; E-LXY7N/E-GFNDF; T-C5VEI/FT-2N57U; D-VAXQT/D-IWIA5;
    T-ZZJDP/FT-5NI77/FT-LGWHM/D-BQLJV/FD-BRJK5; D-VKP6N/FD-BACTZ/FD-ZPKLQ;
    D-AUD6K/FD-C7EQD/FD-EKGLW/PR-NITIQ; D-65VIK/PR-5A64G/PR-ITZIT; PR-VUBCC/PR-EWOP5/E-WNXIR;
    P-DO7TE/E-4GLUR. Candidates: E-SMOHZ isolated-singularity reason; PR-PDYJC needs α<2 but PR-BPP7D
    uses angle 2π; Montel page cites a D-IJMPJ remark; D-YKB3V "Toy contour" heading; E-QVMUV
    "exactly" on the annulus; extra proofs in remarks (PR-K57J6, Schwarz lemma, T-ZZJDP, PR-NITIQ,
    PR-EWOP5, PR-5A64G); possible duplicates E-UVNVV/E-I26BF, PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE,
    D-HHVPT/FD-ST7TD; `STYLE-03` `\mathbb` on maximum-modulus-and-open-mapping and
    cauchy-estimates-and-liouville. Also: D-QTJ7T and T-TUXBP concept blocks that hold only a
    citation. Found while merging: FT-OEYLQ/C-FRF33 (open mapping), FT-5MASA/T-22RQZ (Cauchy
    inequalities). **Acceptance:** each read and repaired, or kept with the reason. **Closed.**
    Every CARD-04 group was one statement and is merged; PR-PDYJC into PR-AQFRA settles PR-BPP7D;
    D-IJMPJ into D-QTJ7T settles the Montel remark; the listed extra proofs left with their merged
    cards. E-UVNVV is kept apart from P-Z776N: it states that $f$ is locally $(n+1)$-to-one, a
    stronger statement. PR-YO7MV/FD-3BK6U, D-2CCDB/FD-XVMEE, D-HHVPT/FD-ST7TD are real-analysis
    cards and stay with `ad2-real-analysis-content` above.
  - **`ad2-site-surfaces`**. **Needs:** none. Renderer: a "problem N" locator is derived when an
    appearance comment is empty; solved counts include child-collection rows
    (SRC-MATH8100-FALL-2019-ASSIGNMENTS, SRC-RA-WORKSHOP); institution ids are upper-cased
    instead of named from the vocabulary; guide titles differ from area names; Pagefind indexes
    the slogan link, backlinks and the collection count; unlabelled page wikilinks show the raw
    path (wiki/archives/qual-workshop-index.md); the home `<title>` repeats the site name;
    SRC-RA-WORKSHOP provenance chips carry no document name. Corpus: E-AMD-4SSSVQJY,
    E-AMD-564ETBH5 and E-AMD-E3N4BHJH are in no collection; stem or truncated titles in
    SRC-RA-WORKSHOP and Berkeley 1977 (`CARD-01`); TeX outside math in titles (P-CAFA22B,
    P-CAFA22D, the 1-connected CW complex card); P-2J6HK remark before hint and solution
    (`STYLE-07`); the topology packets lede names sections that do not exist; SRC-RA-WORKSHOP
    has no institution. Renderer, analysis audit: block `title=` text skips citeproc and smart
    punctuation; "(a)" list markers render as "a."; PR-TC76W "(U)", "(P)", "(N)" parse as a
    list; the E-B4ZSQ diagram `<div>` sits in a `<p>`. Round-2 candidates C5, C6, C8 and C9
    remain for the owner. **Acceptance:** each item read and repaired. **Closed.** Open
    remainder: the three E-AMD orphans come from the maintainer's own review notes, so no
    collection lists them; they duplicate P-Q67AG/P-AMD-62OZUWBP (4SSSVQJY),
    P-MV6ZQ/P-AMD-ZIGVO4GJ/E-JAPBK (564ETBH5) and P-AMD-2NXEX5LK/E-AMD-V3WFKTM6 (E3N4BHJH)
    and wait on `CARD-04` merges. The Day PDFs name no institution, so SRC-RA-WORKSHOP keeps
    none. The "Suggest a slogan" issue link on result cards is a `QUAL-08` candidate for the
    owner. Pagefind may split full institution names at commas. The orphan merges are done
    (`CARD-04`): E-AMD-4SSSVQJY and P-AMD-62OZUWBP into P-Q67AG; E-AMD-564ETBH5, P-MV6ZQ and
    P-AMD-ZIGVO4GJ into E-JAPBK; E-AMD-E3N4BHJH and P-AMD-2NXEX5LK into E-AMD-V3WFKTM6.

  Round 3 (revision `5ba163ac9`, algebra and applied algebra) injected the nodes below;
  `audited-deployment` needs both.
  - **`ad3-renderer`**. **Needs:** none. Citation labels such as `[DuFo04]` and `[Hung74]` on
    wiki and tag pages (D-IPR4B, D-FK47C, PR-E4T3S) render with no bibliography entry or link,
    and the `data-cites` key differs from the label; the `<title>` of P-ALGQUAL18W-I1 carries
    expanded TeX for nested `\sqrt`; the syllabus locator `[@Smi96, sec. 844-1]` renders as a
    section range; `tikzcd` diagrams are still missing on groups pages (D-KRKV7, FF-TSZNT,
    T-NFQBO; open under `ad-tikzcd`). Site surfaces (round 3): the SRC-CALCULUS-PRACTICE-TEST3
    MD chip opens a hand-edited partial `extracted/` file, not the MinerU extraction beside the
    PDF; `problems.html` splits URL filter values on commas, so comma-named institutions match
    nothing; the default problem order puts multi-area cards and `algebraic-geometry` before
    `algebra`; SRC-MATH8100-FALL-2019-ASSIGNMENTS says "0 problems" although its child
    collections hold 70; P-2J6HK renders its remark before its hint and solution (`STYLE-07`);
    search excerpts cut inside math; collection-mode panes with no values show "No data
    available in table"; `?solution=unsolved` reads as an invalid filter when the count is zero.
    Analysis round 3: `(a)` and `(i)` lists render as `(A)` and `(I)` because the `ol[type]`
    selectors in `site/styles.css` lack the case-sensitive `s` flag; appearance comments
    print a literal `--`; the P-4FH62 sub-part labels run on as one list. The `tikzcd` item
    does not reproduce: all three diagrams render at `5ba163ac9`.
    **Acceptance:** each corrected on the deployed pages. **Closed.**
  - **`ad3-algebra-content`**. **Needs:** none. Wrong mathematics: P-APAS18H invariant-ring
    generators omit $xy(x^2-y^2)$; P-APA22F(a) value; PR-OODAV slogan (an abstract
    $B\cong A\oplus C$ does not split); P-RPSTO(b) fixed-field tower indexed backwards;
    P-WBK5B $k=2$ equation; PR-GV5CF proof covers finite families only; classify-this-module
    $\langle 2,x\rangle$ example does not separate flat from torsion-free.
    CARD-04: T-SZRXI/E-NNTQB/E-DKMHL; E-47X7Y/E-VPWK4; PR-PYYRK/E-BSGSM; T-SVJUN/E-R6I7G;
    FT-ZENUU/T-WRMBM/T-EF2MZ/T-S5T5C; PR-IGLFV/E-6AOD7(b)/FF-C3SN4; PR-73MCN/E-PHSV5;
    T-AILFB/PR-LXSGE; D-ZJJ7G/FD-BPUNZ; E-XH2QU/E-HOJKE/PR-DDDXH/PR-GEHJF; T-6ABNR/FT-BC6S2;
    PR-4GQIZ/PR-GBL6P/PR-OF7ZW; D-HGMOW/D-GIGM2; P-HGRO2/P-HGRO4; P-HGRO7/P-HGRO8/P-HGRO31.
    Page restatements (`THEOREM-01`, `DEF-1`): sylow, the-class-equation, is-this-group-abelian,
    orbit-stabilizer, series-and-solvability, groups-of-small-order, fields/extensions,
    splitting-and-normal, separability, the-correspondence, worked-examples,
    compute-this-galois-group, ideals-and-quotients, domains-and-factorization (valuation ring
    and DVR, D-DEFREGLR), commutative-algebra, number-theory, which-kind-of-ring,
    free-and-projective, classify-this-module, exact-sequences, characters, the-spectral-theorem,
    minimal-and-characteristic-polynomials, determinants-and-eigenvalues, matrix-counterexamples.
    Notation (`NOT-3`): series indexing and the D-BGNME lower central series; `\maxspec` against
    `\mspec` (E-AMD-V3WFKTM6, E-AMD-DCVAD27P, P-W8CJF, E-AMD-EBIC3Z5S); over-a-pid $M_{(p)}$;
    the sylow exponent letter. Titles: E-BAOST (`CARD-01`), P-APAS18D "octogon", P-HGRO* group
    names (`CARD-06`). Screenshots: compute-this-galois-group $S_4$ tables, review-sheet-1
    homework 1 image, minimal-and-characteristic-polynomials long division. Topics
    (`TAXON-01`): the-correspondence, worked-examples. `STYLE-08`: P-ZIMYA, E-XH2QU, E-HOJKE,
    E-VFEWT, E-G4KAC, E-M6J67, P-AMD-QBEEJKCX, E-LJ7PF, P-4XOCE (attribution, $C_x$ notation,
    bullet solution), P-VI6QM literal lists, P-APAS18A–H, P-APA22A–H, P-APAF20A/D/H, the
    P-ALGQUAL18W cards. Scope: E-G4KAC noncommutative on a commutative page; which-kind-of-ring
    Gorenstein section; determinants-and-eigenvalues matrix groups over $F$ linked to
    $\RR$/$\CC$ cards. Sources: SRC-AMHERST-ALGEBRA-STUDY-GUIDE-2016 exam dates in statements
    (`CARD-02`); SRC-HARVARD-GROUPS-ORAL invented sections and institution (and the COMM-ALG
    and FIELDS orals); rings-and-ideals/solutions Gallian headings and MIT pointer; groups
    resources "Chapter N solutions" (`RES-01`). **Acceptance:** each read and repaired, or kept
    with the reason. **Closed.** Merges (survivor first): E-NNTQB/T-SZRXI/E-DKMHL;
    E-47X7Y/E-VPWK4; E-BSGSM/PR-PYYRK (a collection lists E-BSGSM); E-R6I7G/T-SVJUN;
    T-WRMBM, T-EF2MZ, T-S5T5C/FT-ZENUU; PR-73MCN/E-PHSV5; T-AILFB/PR-LXSGE; D-ZJJ7G/FD-BPUNZ;
    E-HOJKE/PR-DDDXH; FT-BC6S2/T-6ABNR; PR-4GQIZ/PR-GBL6P/PR-OF7ZW; D-GIGM2/D-HGMOW. Kept
    apart after reading: E-6AOD7 and PR-IGLFV (PR-IGLFV also classifies the groups; FF-C3SN4
    now cites it); PR-GEHJF loses only its items owned by E-XH2QU and E-HOJKE; P-HGRO2/P-HGRO4
    (P-HGRO2 also counts order 35); P-HGRO7, P-HGRO8, P-HGRO31 (state against two different
    proofs); P-AMD-QBEEJKCX already argues in its QED step. The three oral sources name no
    institution and list Berkeley examiners from the MGSA files, so they are now
    SRC-MGSA-GROUPS-ORAL, SRC-MGSA-COMM-ALG-ORAL and SRC-MGSA-FIELDS-ORAL with no institution
    and one source section each. The homework 1 image became SRC-FIELDS-HOMEWORK-1 (PDF wrapped
    from the retained JPEG, MinerU extraction). `\maxspec` is retired for `\mspec`. The
    Gorenstein section moved to commutative-algebra. Open remainder: SRC-HARVARD-COMPLEX-ORAL
    has the same unsupported institution; the oral PDF and extraction filenames still say
    Harvard; P-FHW1 cards overlap PR-ABSJX, PR-OFBRQ, P-HBWYH and P-JXIIG and need a `CARD-04`
    reading; no card exists for the mod-$p$ irreducibility test, the degree-2-or-3 root test,
    finite extensions of finite fields being Galois, or algebraic closure; the D-2IO6Q
    noncommutative remark has no citation; orbit-stabilizer still restates the element-order
    clause of E-NNTQB.
  - **`ad3-algebra-followups`**. **Needs:** none. The open remainder of `ad3-algebra-content`:
    SRC-HARVARD-COMPLEX-ORAL institution; oral PDF and extraction filenames that say Harvard;
    `CARD-04` reading of the P-FHW1 cards against PR-ABSJX, PR-OFBRQ, P-HBWYH and P-JXIIG;
    statement cards for the mod-$p$ irreducibility test, the degree-2-or-3 root test, finite
    extensions of finite fields being Galois, and algebraic closure; a citation on the D-2IO6Q
    noncommutative remark; the E-NNTQB restatement on orbit-stabilizer. `audited-deployment`
    needs it. **Acceptance:** each read and repaired, or kept with the reason. **Closed.**
    The complex-analysis oral names no institution (MGSA files, McMullen, Calegari), so it is
    SRC-MGSA-COMPLEX-ORAL with one source section; the four oral PDFs and extractions are
    `MGSA_*`. PR-ABSJX merged into P-FHW1-02. Kept apart after reading: P-FHW1-05 (adds the
    characteristic-2 failure) from PR-OFBRQ and P-JXIIG, and P-FHW1-11 from P-HBWYH (adds
    $\alpha^{2020}$). The mod-$p$ test already existed as PR-PB6UE and is now on the
    polynomials page; new cards PR-I1T7M (root test), PR-OGUA5 (finite-field extensions) and
    D-99IUP (algebraic closure). D-2IO6Q cites Hungerford IX.2; orbit-stabilizer drops its
    Lagrange corollary, now carried by E-NNTQB. Open item moved from
    `ad3-real-analysis-content`: the workshops guide lists P-6XW74 and P-KPEPM twice in its
    algebra weeks. **Closed.** Both listings are kept: the Algebra Week 1 and Week 2 sheets
    (`assets/Workshops/Algebra/`) each pose both problems, and each guide week follows its sheet.
  Round 3 (revision `5ba163ac9`, analysis provenance) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-analysis-provenance`**. **Needs:** none. Round-3 analysis findings C1-C4: 16 UCLA
    real-analysis collections list the solution writeup `UCLA_Solutions.pdf` as provenance;
    SRC-UGA-CA-COMPILATION lists maintainer PDFs, wrong section labels and a repeated entry;
    eight UGA complex-analysis collections link dead department PDFs; one PDF is split across
    several collections (Lyall MATH4100-6100 A1-A9, the Wesleyan real- and complex-analysis
    PDFs, Cracking the GRE). **Acceptance:** no collection lists a solution writeup or a
    maintainer PDF; each UGA href resolves to a vendored paper; each PDF is one collection
    whose papers are sections, with every problem link kept. One collection at a time.
    **Closed.** The UCLA collections list the department papers `analysis-YYS.pdf`;
    SRC-UGA-CA-COMPILATION has empty provenance (no external original found; its sections and
    repeats follow the PDF); the eight UGA papers are vendored from the Wayback Machine; the
    compilations are SRC-MATH4100-6100-2020, SRC-WESLEYAN-ANALYSIS-2003-2007, -2008-2013,
    -2014-2016 and SRC-GRE-MATH-SUBJECT. `CompilationSource` has no `institution` and one
    `area`, so the Wesleyan compilations lose the `wesleyan` institution and carry
    `area: real-analysis` for mixed real and complex papers. The Wesleyan topology PDFs are
    still split across collections.
  Round 3 (analysis provenance follow-up) injected the nodes below; `audited-deployment` needs both.
  - **`ad3-compilation-schema`**. **Needs:** none. `CompilationSource` has no `institution`
    and one `area`, so mixed-area compilations mislabel their papers; the Wesleyan topology
    PDFs topology_2005-2003.pdf and topology_2006-2014.pdf are split across 14 collections;
    round-3 provenance findings C5-C12 that no other node owns. **Acceptance:** a compilation
    carries `institution` as an exam source does and takes its areas from the one mechanism
    every source kind shares; the three SRC-WESLEYAN-ANALYSIS compilations name `wesleyan`
    and their real areas; each Wesleyan topology PDF is one compilation with one section per
    exam and every entry kept; each unowned C5-C12 finding read and repaired, or kept with
    the reason. **Closed.** C8 locators, C9 and C10 are repaired; C6 vendoring runs in a
    separate stream. The rest is kept in `ad3-provenance-residue`, because each item needs
    a source read or a card split.
  - **`ad3-provenance-residue`**. **Needs:** none. Kept round-3 provenance findings:
    the UNSORTED buckets (about 1500 problems) are not dissolved into source collections
    (C5); SRC-CA-ART-E3SXDB, SRC-CA-ART-T34TG3, SRC-NUS-CA-1970-SPRING and
    SRC-NUS-RA-1970-SPRING have no provenance (C5); JHU September 2019 complex Problem 4
    has no card in SRC-JHU-ANALYSIS-EXAMS (C7); P-DUKEBA14-9 adds a domain change of
    coordinates that the source does not ask for (C8); the UCLA 2009 and 2010 real-analysis
    collections are not checked for complex-analysis problems (C11); P-4FH62 holds 17
    problems that six UGA exams cite as one card (C12). **Acceptance:** each item repaired
    against its source PDF. **Closed.** UNSORTED moved to `ad3-unsorted-dissolution`.
    C7: Problem 4 was P-7QJS2; Problem 3 was merged into P-8XT21 and is now P-SBKCW. C8,
    C11 (four UCLA 2009-2010 papers) and C12 (P-4FH62 split; the six UGA exam parts are
    listed by their exams, eleven parts stay in the real-analysis bucket) are repaired. C5:
    no qualifying href found in this repository or sibling clones (only make-me-a-qual and
    qual-review-and-solutions copies, which are not provenance); the web search service
    failed, so the four lists stay empty. Closing note (2026-10-30): a web search on
    distinctive problem text (NUS zero count of $2z^5-6z^2-z+1$, the region between
    $\abs z=1$ and $\abs{z-1/2}=1/2$, the finite-cover outer-measure statement, the
    Spring 2020 homework statements) found no external document for the four collections,
    so their provenance stays empty. UCLA Fall 2010 Problems 1, 7 and 10 are existing cards
    P-4KTFN, P-B4WQK and E-7ZCKU, now listed in SRC-UCLA-RA-FALL-2010 in source order.
  Round 3 (provenance finding C5) injected the node below; `audited-deployment` needs it.
  - **`ad3-unsorted-dissolution`**. **Needs:** none. The UNSORTED buckets (about 1500
    problems) are not dissolved into source collections. For each card, one at a time: find
    the document its statement came from (an exam PDF under `assets/attachments/`, a sibling
    clone's source, or a web search on distinctive text); list it in that document's
    collection, or create the collection with real provenance (one PDF is one collection);
    remove it from the bucket only after the source listing is confirmed; leave it in the
    bucket when no source is found. Never invent provenance.
    - [x] SRC-UNSORTED-ALGEBRA: 660 cards tried, no source found
    - [x] SRC-UNSORTED-COMPLEX-ANALYSIS: 232 cards tried, no source found
    - [x] SRC-UNSORTED-REAL-ANALYSIS: 83 cards tried against the exam extractions, Folland,
      and Stein--Shakarchi I and III; no source found
    - [x] SRC-UNSORTED-TOPOLOGY: 91 cards tried, no source found
    - [x] SRC-UNSORTED-PRELIM: empty
    **Acceptance:** every bucket card tried; each bucket's count of cards with no source found
    is recorded here.
  CI on `main` is red from the STYLE-04 bar codemod (`1f17231d05`) on; nothing deploys after
  `5ba163ac9`. `audited-deployment` needs the node below.
  - **`ci-red-style04`**. **Needs:** none. The codemod left a space before closing dollars
    (`$\norm{ f } $`), so the `reports` job fails on "a $ reached the page as text"; repair the
    spacing only. `qc-ci / qc` fails on two `test_static_site.py` assertions left stale by the
    tab listing key and recursive collection counts. The changed-card push check runs the
    unread-math check on each changed card, without loading the corpus.
    **Acceptance:** a green `development.yml` run deploys, and `revision.txt` names its commit.
  Round 3 (revision `5ba163ac9`, topology and algebraic geometry) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-topology-content`**. **Needs:** none. Wrong mathematics: P-TOPS05A (a free
    involution of $S^{2n}$ need not be the antipodal map; the quotient need not be
    homeomorphic to $\RP^{2n}$); P-TOPS06B title (higher-genus surfaces do cover lower-genus
    ones); P-TOPF23D title ("is" for "is homotopic to");
      wiki/algebraic-geometry/varieties/index.md
    (affine varieties correspond to finitely generated domains, not reduced algebras);
    sheaves-of-modules/projective-sheaves.md (very ample gives an immersion, closed when $X$ is
    proper); cw-complexes RREF row span over $\ZZ$; P-AT75W "$U \in X$"; P-TOPF09C
    $H_*$/$H^*$ hedge. `QUAL-10` proofs of standard results: fundamental-group/theorems.md
    (T-2YTCZ, T-BTPU4, PR-3APOT, PR-OO3DH, PR-EWJMJ), point-set.md tube lemma, homology.md
    PR-6PENU, D-FAIJX Mayer--Vietoris remark, FT-6WPJI corollary proof, FT-M5BHD (twice),
    D-KC4BS Moore spaces; review-page sentences that advertise them. `CARD-04`:
    D-WX7JH/PR-BQKHS (and the D-6CI7D remark that redefines $\tilde M$); D-QP7WI/PR-4X6G2;
    D-6UHU7/D-UH3L5; T-N6PYS/FT-M5BHD; T-TJBYR/PR-ZCUXL(1); PR-UBJ6P/D-BX3WD; T-O44GI/PR-HQE2T;
    D-GFM35/PR-EWJMJ; PR-B6BB2/D-IGUUS proposition; T-NBARV/FF-GBHJL/FF-IEHB2/FF-W3AIU
    (PR-LIXWH); P-FHLRF/P-24CMJ/P-CEVX4; P-VTB25/P-D6JY5/P-6HH2P. `THEOREM-01`, `DEF-1`:
    every topology guide lede in publications/topology-guide.yaml (British spellings too);
    D-WSFYS van Kampen remark; compute-pi-1 and compute-h-star local theorem blocks; AG pages
    what-is-a-scheme, subschemes-and-points, proj-and-gluing, fibre-products-and-base-change,
    the-sheaf-condition, stalks-and-exactness, line-bundles, differentials, canonical-class.
    Pages: topology resources/problems.md links raw PDFs (`RES-01`); point-set.md
    "Separability" heading; notation-and-background degree convention (`NOT-3`);
    the-standard-spaces-notes orphan page; surfaces-and-manifolds stray complex-manifold
    sentence and duplicated T-NBARV sentence; PR-SCHINT link text; covering-spaces diagrams
    (renderer, `ad-tikzcd`). Collections (`SEC-7`, `SOURCE-03`): appearance comments on
    SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007, SRC-UGA-TOP-FALL-2004/2009/2012,
    SRC-WESLEYAN-TOP-2004/2014/SUMMER-2008/SUMMER-2011/SUMMER-2013, and the SRC-UNL-MATH871
    grading notes; Perutz, UNL 871 and UT M392C bare section names; Maxim "Poincare Duality ´".
    Card defects: SRC-UGA-TOP-FALL-2013 problem 9 fixed-point title; P-AGXHWSUPPORT alignment;
    P-AGXVARSURFACESING doubled link text; P-WESTOP05-10, P-QUAL-REVIEW-HATCHER-10 and -11
    undefined symbols and in-solution headings; P-AGXHWREDUCED and P-8TF16 part labels.
    Titles (`CARD-01`, `CARD-06`): Malone--Housley imperative titles; raw ASCII TeX titles on
    the UCSD, MAT367, UGA 8230, PhD F08 and workshop collections.
    - Locator titles (`CARD-02`), one card at a time: P-AT75W, P-MAXAT-1-01, P-MAXAT-1-02,
      P-MAXAT-1-03, P-MAXAT-1-04, P-MAXAT-1-05, P-MAXAT-1-06, P-MAXAT-1-07, P-MAXAT-1-08,
      P-MAXAT-1-09, P-MAXAT-1-10, P-MAXAT-1-11, P-MAXAT-1-12, P-MAXAT-1-13, P-MAXAT-2-01,
      P-MAXAT-2-02, P-MAXAT-2-03, P-MAXAT-3-01, P-MAXAT-3-02, P-MAXAT-3-03, P-MAXAT-3-04,
      P-MAXAT-3-05, P-MAXAT-3-06, P-MAXAT-4-01, P-MAXAT-4-02, P-MAXAT-4-03, P-MAXAT-4-04,
      P-MAXAT-4-05, P-MAXAT-4-06, P-MAXAT-4-07, P-MAXAT-4-08, P-MAXAT-4-09, P-MAXAT-4-10,
      P-MAXAT-4-11, P-MAXAT-4-12, P-MAXAT-4-13, P-MAXAT-5-01, P-MAXAT-5-02, P-MAXAT-5-03,
      P-MAXAT-5-04, P-MAXAT-6-01, P-MAXAT-6-02, P-MAXAT-6-03, P-MAXAT-6-04, P-MAXAT-6-05,
      P-MAXAT-6-07, P-MAXAT-6-09, P-MAXAT-6-10, P-MAXAT-6-11, P-MAXAT-6-12, P-MAXAT-6-13,
      P-UNL872S14-10-A-1, P-UNL872S14-10-A-2, P-UNL872S14-10-A-3, P-UNL872S14-10-A-4,
      P-UNL872S14-10-B-1, P-UNL872S14-10-B-2, P-UNL872S14-10-B-3, P-UNL872S14-10-C-1,
      P-UNL872S14-10-C-2, P-UNL872S14-10-C-3, P-UNL872S14-10-C-4, P-UNL872S14-11-B-1,
      P-UNL872S14-11-B-2, P-UNL872S14-11-C-1, P-UNL872S14-11-C-2, P-UNL872S14-11-C-3,
      P-UNL872S14-11-C-4, P-UNL872S14-12-A-1, P-UNL872S14-12-A-2, P-UNL872S14-12-B-1,
      P-UNL872S14-12-B-2, P-UNL872S14-12-B-3, P-UNL872S14-6-A-1, P-UNL872S14-6-A-2,
      P-UNL872S14-6-A-3, P-UNL872S14-6-A-4, P-UNL872S14-6-A-5, P-UNL872S14-6-B-1,
      P-UNL872S14-6-B-2, P-UNL872S14-6-B-3, P-UNL872S14-7-A-1, P-UNL872S14-7-B-1,
      P-UNL872S14-7-B-2, P-UNL872S14-8-A-1, P-UNL872S14-8-A-2, P-UNL872S14-8-A-3,
      P-UNL872S14-8-B-1, P-UNL872S14-8-B-2, P-UNL872S14-8-C-1, P-UNL872S14-9-A-1,
      P-UNL872S14-9-B-1, P-UNL872S14-9-B-2, P-UNL872S14-9-B-3, P-UNL872S14-9-B-4,
      P-UNL872S14-9-C-1, P-UNL872S14-9-C-2, P-UNL872S14-9-C-3, P-UNL872S14-PP-1,
      P-UNL872S14-PP-2, P-UNL872S14-PP-3, P-UNL872S14-PP-4, P-UNL872S14-PP-5.
    - `**Goal**` paragraphs (`STYLE-08`), one card at a time: E-013M4, E-01BSA, E-04W6Q,
      E-069N4, E-0A010, E-0EZ4U, E-0GRG4, E-0K3QV, E-0LZE7, E-0MY4M, E-0NSGA, E-160XR, E-175IG,
      E-18MBF, E-1CMTE, E-1DM8W, E-1P97G, E-1QGID, E-1QY2X, E-1VSTU, E-24TY3, E-29WP0, E-2B91X,
      E-2BCY2, E-2BNJ6, E-2M0XQ, E-2NLYP, E-2P51H, E-2V2VL, E-3BSN7, E-3CFLD, E-3FN03, E-3JLUV,
      E-3KMYL, E-41BN2, E-432BL, E-4349Q, E-44O6O, E-4E1C9, E-4KGM4, E-4PQ1O, E-4RF8O, E-4S8XS,
      E-4TG52, E-4WKOG, E-4WQEM, E-52GF4, E-57O2M, E-5CC0M, E-5DDIL, E-5FLKZ, E-5GHY2, E-5NREC,
      E-5VNUL, E-5VWPC, E-5WDER, E-5Y4F7, E-66MV0, E-6C2JI, E-6RQWT, E-70TGS, E-71YOD, E-73JHB,
      E-74C1G, E-79XXG, E-7GVUH, E-7ML5F, E-81J56, E-873VF, E-8EX2G, E-8HR3A, E-8IBEP, E-8NCA4,
      E-8Q9TN, E-8T3QS, E-8VZD4, E-97HXB, E-99H07, E-9IP2I, E-9LY2B, E-9OT3C, E-9RR0I, E-9TQ6L,
      E-A3WS1, E-A7HJX, E-AGJM5, E-AHENA, E-AL52O, E-CJA01, E-DUQHF, E-E79BA, E-HAT-1.1-11,
      E-HAT-1.2-19, E-HAT-1.2-3, E-HAT-1.2-7, E-HAT-1.3-20, E-HAT-1.3-9, E-HAT-1.B-4,
      E-HAT-2.1-7, E-HAT-2.2-2, E-HAT-2.2-42, E-HAT-2.C-2, E-HAT-3.2-14, E-HAT-4.1-13,
      E-HAT-4.1-18, E-HAT-4.2-5, E-HAT-4.2-8, E-HAT-4.3-19, E-HAT-4.D-6, E-HAT-4.H-4, E-LV54B,
      E-MUN-6-5, E-VFXN4, P-AMD-2AFAX7LD, P-AMD-2GG7VEF2, P-AMD-4DYUOGAJ, P-AMD-5TW33AUF,
      P-AMD-6GFMKZVQ, P-AMD-6KL53YZC, P-AMD-6OJQMSOZ, P-AMD-6QDQY5HT, P-AMD-6RPCGOV7,
      P-AMD-7IWMHJHE, P-AMD-A2CPGINL, P-AMD-ALXD5IQN, P-AMD-AZWPAEUQ, P-AMD-D7IX7C4G,
      P-AMD-DDQM3X6Q, P-AMD-DX7L7EFB, P-AMD-E67LQFU5, P-AMD-EPCKWZSV, P-AMD-ES2H5QQF,
      P-AMD-F7UPRCWM, P-AMD-FW4WE7JA, P-AMD-GEBWFMJF, P-AMD-IUGBCO5R, P-FZIG3, P-KVMKV,
      P-LSJ7W, P-MHQ6A, P-PATOJ, P-SAEXG, P-TOPF08E, P-TOPF09G, P-TOPF20E, P-TOPF20H,
      P-TOPF21C, P-TOPF22E, P-TOPF24G, P-TOPF24H, P-TOPS13B, P-TOPS25G, P-UCTOP-SU09-8,
      P-UCTOP-SU14-7, P-WOFN2.
    - Solutions with no structured proof (`STYLE-08`), one card at a time: P-AGXHWGLOBALSECEX,
      P-AGXHWREDUCED, P-AGXHWSKYSCRAPER, P-AGXHWSUPPORT, P-AGXMISCPRODRATIONAL,
      P-AGXGATHVICLOSURE, P-AGXNSSNONCLOSED, E-MAT367-01, E-PER08-21.3, E-PER08-21.5,
      E-PER08-21.7, E-PER08-23.1, E-PER08-23.4, E-PER08-24.1, E-PER08-24.3, E-PER08-26.2,
      E-PER08-26.3, E-PER08-6.7, E-PER08-7.1, E-PER08-9.3, P-PSTM-01, P-PSTM-02, P-PSTM-03,
      P-PSTM-04, P-PSTM-05, P-PSTM-06, P-TOPF10C, P-DDUA3, P-IWMWM, P-AT75W.
    - Proof gaps found during the Goal repair: E-HAT-2.2-42 (finiteness of $G$ unused,
      unproved existence step); E-HAT-3.2-14 ($\CP^1\to\HP^1$ degree, $\abs{\beta}$, the
      $\HP$ case); E-HAT-1.2-19 (perturbation over infinitely many spheres, continuity at
      $t=1$); E-8EX2G (annulus quotient is a Möbius band); E-8NCA4 (match with Munkres §68
      Example 1); E-79XXG (figure-dependent claims); E-HAT-4.3-19 (statement $\langle X,B\rangle$
      against $\langle X,\Omega B\rangle$, checked against Hatcher).

    **Acceptance:** each read and repaired, or kept with the reason. **Closed.** The wrong
    mathematics, QUAL-10 deletions, CARD-04 merges, ledes, titles, Goal paragraphs, 30
    structured proofs and seven proof gaps are repaired, each in its own commit. Near-duplicates
    whose mathematics differs became Variations remarks on the survivor. Historical ledgers
    under `sources/` keep the merged ids.

  Round 3 (revision `5ba163ac9`, site surfaces and prelims) injected the nodes below;
  `audited-deployment` needs both.
  - **`ad3-prelim-content`**. **Needs:** none. F8: prose solutions with no structured proof
    (`STYLE-08`) on P-PRACT20-W3-13, P-PRACT20-W4-06, P-PRACT20-W3-18, P-ALGPAN11-01. F9: wrong
    area on P-PRACT20-W4-06 (`applied-algebra`), P-PRACT20-W3-13 and P-PRACT20-W3-18
    (`real-analysis`). F10: P-ALGPAN11-01 answer choices only in an image (`CARD-03`). F11: the
    20 P-CALCPT3 cards have no topics (`TAXON-01`). F12: wiki/prelim/problems/berkeley-prelims.md
    and ucla-prelims.md link raw PDFs where a collection owns the exam (`RES-01`). F13: prelim
    wiki `order` does not follow wiki/prelim/index.md (`NAV-01`). F14: worked-exams pages hold
    no worked material, and the index link label differs from the page title. F15:
    "$\deg P + 1$ integrations by parts" on useful-tricks.md and which-technique.md.
    **Acceptance:** each read and repaired, or kept with the reason. **Closed.** The worked-exams
    pages are kept and renamed UGA prelim exams; the Berkeley syllabus PDF has no collection
    and stays a PDF link.
  - **`ad3-prelim-practice-areas`**. **Needs:** none. F9 extends past its three cards:
    SRC-PRELIM-PRACTICE-WEEK3-2020 (`real-analysis`), SRC-PRELIM-PRACTICE-WEEK4-2020
    (`applied-algebra`) and the other P-PRACT20-W3-* and P-PRACT20-W4-* cards carry core-qual
    areas for prelim practice drills (COMPLAINTS.md "2020 prelim practice weeks 3 and 4").
    **Acceptance:** each card and both collections read and given the area of the exam track
    they belong to. **Closed.** All 54 cards and both collections are `prelim`.

  Round 3 (revision `5ba163ac9`, real and complex analysis) injected the node below;
  `audited-deployment` needs it.
  - **`ad3-complex-analysis-content`**. **Needs:** none. Wrong mathematics: analytic-nt
    Dirichlet-test proof with the sequences swapped; P-W23PS ($O(R^{1-n})$, two integrals named
    $I$, lost $i$, two solutions); E-NZY3B image; P-CZ3R7 algebra and circle; P-37Z7J identity;
    E-3B2YA intermediate value; P-ER23C Rouché count; maximum-modulus-and-open-mapping $f(U)$;
    E-XQX6X, E-XKMVX Schwarz lemma on the closed disc; T-6F3GO codomain and D-TIHRR
    equicontinuity; P-CASP17A title bounds; complex-week-2-cauchy $\int_{\partial T}$.
    `QUAL-10` wiki proofs: computing-residues, arc-estimates, the-argument-principle,
    rouches-theorem, the-integral-formula, max-modulus, cauchys-theorem, cauchy-estimates,
    maximum-modulus-and-open-mapping, analytic-nt. Process text (`QUAL-08`): P-CASP17A,
    P-CASP15E, P-CASP17D, P-W23PS, P-TIE-S14-03, HARVARD-MATH213A-2017 "(repeats Exercise 3)",
    E-UVNVV and E-QVMUV step prose, Wesleyan complex extractor titles, tips-techs [Eur15].
    Titles (`CARD-01`, `CARD-06`) on the complex UCSD and UGA cards. `CARD-04`: the complex
    groups of the round-3 analysis report, section F. Restatements (`DEF-1`, `RENDER-02`):
    report H1-H8 and H12-H16. `STYLE-04`/`STYLE-08` on the complex cards of report section I.
    Guides: complex guide `parent:` chains (`NAV-01`) and the "grouped by type" ledes.
    Moved from `ad3-real-analysis-content`: E-M5MWL interval $(-1,1]$; "exact existing owner"
    appearance comments on the Wesleyan complex-analysis exams; titles of P-AEWN6, E-SS4.PR-2,
    E-SS9.PR-1 and FT-FZERI. Also moved: complex cards of report section I (P-Y5SS5,
    E-TZJKN, E-WNXIR, P-Z776N, E-SS1.EX-13, E-THK2Z, P-7UIYI, P-HCAX18, P-CHAVAN-CA-3-7,
    P-CM16-S2-08, P-TWN5M, P-FOXHV, P-7UTDI, P-F7HCN, E-SS1.EX-19, P-K4WSJ, E-VGNUI, E-WIANB,
    P-EMCA9, E-SS2.EX-15, P-AQRVL, P-MMAQ-WPHHQBXBQ3, P-MMAQ-YUXDCVQRF5, P-RGBUN,
    P-AZOFF-G04, P-TIE-F11-02, E-SS2.EX-2, P-PSIBT, UNSORTED-COMPLEX "Rudin 10.4" comments);
    T-ZO5UU and T-SSNLT alt text; the 40 complex UCSD titles with a bare `^`
    (P-CAF09A through P-CASP26C); P-UCLARA14S-12 is a complex problem filed as real analysis.
    **Acceptance:** each read and repaired, or kept with the reason. **Closed.** Kept: E-SS1.EX-19 id (ids are not renamed); corpus-wide `STYLE-04` forms are codemod work in COMPLAINTS.md.

  Round 3 (revision `5ba163ac9`, real analysis) injected the node below; `audited-deployment`
  needs it.
  - **`ad3-real-analysis-content`**. **Needs:** none. Open items. Process text (`QUAL-08`, `SEC-7`): P-3SSNK source tag; SRC-RA-WORKSHOP locators in
    statements (D6-10, D4-07, D8-SEQ1). Titles (`CARD-01`, `CARD-06`): UMN, UCLA, UCSD, JHU,
    Math8100 and UGA formula-in-words titles, P-RA-WORKSHOP-D8-SEQ1, appendix-unsorted, P-RA-WORKSHOP-D3-SEQ-14, T-S3C3S, UCSD titles
    with a bare `^`. Figures: T-OXNTU, T-ZO5UU, T-SSNLT, PR-YO7MV alt text. P-4FH62 sub-part
    labels. `CARD-04`: D-YWRVG/D-3PVRB; PR-XAVMU/FR-7YFAU; T-QBTWN/T-W5SDY; PR-A7UFG/PR-PRSKG;
    FE-LJRG2/FE-VT5N3/FE-BFDRF/FE-3RPMC against PR-TC76W; P-VO7MI/P-2B2T5/P-8RB01;
    D-HHVPT/D-WGYSB; D-TVKFM/D-KJBAK; D-PAEDW/D-HOKQD; FS-5FKPD/FF-IAUQG; FS-FZL2X/PR-WUZSG;
    condensation block against PR-4EVYE; negation block against FS-THMMW; PR-25GM2/T-YOZX6;
    FF-AVBFU Lebesgue criterion against PR-TDH2A; repeated commuting-limits counterexamples;
    advice H⊔N bullet against PR-PIVFR; P-PCOHF/P-T7IKN; P-5CM5W/P-KC3PY;
    P-DFDX4/P-RA-WORKSHOP-D8-SEQ1; P-UMNCP-F12-01/P-JHUSP02CAF; P-3IDAX/P-ZZO3P;
    T-AZSCN/FF-IAUQG; FD-XUGN3 remark; the Folland exercise list on preface.md and problems.md.
    `QUAL-10` proofs: T-OTR5M, PR-6OHTJ, T-MN6WQ, T-RIY2P, T-BFOJT, T-DTXIA, T-4BDE3, T-J3AN3,
    T-ERNLN, FF-IAUQG, D-YZC3C; the advice.md measurability proof under the graph (read whether
    it is a standard result); the theorem-list pointer to littlewood-principles-notes.
    Restatements (`DEF-1`, `THEOREM-01`): the measure-level pages, undergrad-appendix, week 2,
    sets-and-compactness. `STYLE-04`/`STYLE-08`: typed steps, vacuous QED steps, "a." part
    lists, notation and form on the real-analysis cards of the round-3 report (I1-I16, including
    P-XEEUX, P-VACDU, P-JPDRQ, P-E33SA). Guides: `NAV-01` parent chains in
    publications/real-analysis-guide.yaml; the real-analysis-workshop-packet lede cites numbers no card shows.
    **Acceptance:** each read and repaired, or kept with the reason. **Closed.**
    Kept apart after reading: D-PAEDW (sequences of sets) and D-HOKQD (real sequences);
    D-TVKFM keeps its own content and links D-KJBAK for density. P-8RB01 was P-VO7MI and
    P-2B2T5 joined as (a) and (b), so it was deleted and the two single cards kept. Unchanged
    and already correct: UGA real-analysis titles, the appendix-unsorted title, continuity.md,
    P-OPH7A, P-4FH62. Week 2 (lim sup and lim inf, Lebesgue-Stieltjes regularity) and
    undergrad-appendix (differentiation and Baire facts) still state results that have no card.
    Now carded and transcluded: week 2 uses the existing D-PAEDW and new T-7X52J
    (Lebesgue--Stieltjes regularity); undergrad-appendix uses new T-SM8EW (bounded variation
    and absolute continuity), T-YKOLU (Lebesgue density) and PR-63NN6 (meager and residual sets).

  Round 3 (site surfaces) injected the node below; `audited-deployment` needs it.
  - **`ad3-duplicate-extractions`**. **Needs:** none. 133 PDFs under `assets/attachments/`
    each have two extractions, `<stem>_extracted.md` beside the PDF and
    `assets/attachments/extracted/<stem>.md`, and the MD chip can open the wrong one.
    **Acceptance:** each PDF keeps one extraction beside it whose MinerU Flash or Mistral OCR
    provenance the repository establishes; the other copy is trashed and every reference to it
    repointed; a PDF with neither copy established is regenerated with MinerU Flash. **Closed.**
    chapter-6.pdf is a degraded scan: its per-page Flash extraction garbles Questions 1 and 5,
    and a Mistral OCR pass is still owed when the API accepts requests.

  Round 3 (finding I4, [COMPLAINTS.md](COMPLAINTS.md)) injected the node below; `audited-deployment` needs it.
  - **`ad3-style04-notation`**. **Needs:** none. `STYLE-04` delimiter and definition forms are
    corpus-wide: 166 cards write `\definedas` and about 1913 cards write raw `|` bars.
    **Acceptance:** `\definedas` is rewritten to `\coloneqq` by one codemod; each raw bar pair is
    classified once by its meaning (absolute value, norm, cardinality, set-builder separator,
    divisibility, restriction or evaluation, conditional) and the same codemod applies the
    vocabulary macro for that meaning; each changed card's Pandoc AST differs only in those
    substitutions; the card check in `tools/qualc/authoring.py` rejects the raw forms; the
    codemod is trashed after the rewrite is committed. **Closed.**

  Round 4 (revision `e6068b271c`, prelim collections) injected the node below;
  `audited-deployment` needs it.
  - **`ad4-prelim-content`**. **Needs:** none.
    - [x] CARD-04: P-BKS21-2A and P-BKF10-1A state one problem (Spring 2021 reprints Fall 2010
      1A); merge, survivor listed by both collections.
    - [x] CARD-04: P-BKS21-3A and P-BKF10-5A; same.
    - [x] CARD-04: P-BKS21-4A and P-BKF10-7B; same.
    - [x] P-UCLAB06W-09: the paper prints $A = A^t$, the card silently reads $A^{-1} = A^t$; the
      printed statement is false (diag(2,2,1/4)). Transcribe the printed hypothesis and record
      the correction in a remark.
    - [x] P-UCLAB06W-03: the paper prints prefactor $1/n$, the card silently reads $(b-a)/n$;
      same treatment.
    - [x] Read the other Berkeley online-era papers (Fall 2020, Spring 2021 Part B) for further
      reprinted problems carded twice. Spring 2021 reprints fourteen more 2011--2012 problems
      (merged); Fall 2020 and Spring 2021 6B have no earlier card.
    **Acceptance:** each item read and repaired. **Closed.**

  Round 4 (revision `e6068b271c`, algebra guide) injected the node below; `audited-deployment`
  needs it.
  - **`ad4-algebra-content`**. **Needs:** none.
    - [x] E-HOJKE solution and Variations remark: a line beginning "(3) implies (1)" or
      "(2) implies (1)" renders as an ordered list. Repair the cards, and find whether the
      parser should reject a line-initial parenthesized numeral that is not a list
      (owner of `ad-fancy-lists`). No check: a part label "(b)" opening a paragraph after display
      mathematics is the same one-item list and is authored in many problem statements.
    - [x] FD-T7IQV proof mixes $G^i$ and $G_i$ for one series (NOT-3).
    - [x] CARD-04: D-RG5FO and D-H4TDM both define the Gram matrix of a bilinear form and its
      change of basis; merge, keeping distinct content. D-RG5FO shows "Suggest a slogan".
    - [x] PR-GEHJF remark: the sentence built around inserted card titles is ungrammatical.
    **Acceptance:** each item read and repaired. **Closed.**

  Round 4 (revision `e6068b271c`, algebraic-geometry wiki) injected the node below;
  `audited-deployment` needs it.
  - **`ad4-ag-content`**. **Needs:** none. **Closed.**
    - [x] T-BIRINV (blowups-and-classification): link text makes "Fano, Calabi--Yau" read as
      birational invariants; only general type (Kodaira dimension) is.
    - [x] PR-IV2INSEP closing paragraph: "isomorphic as schemes, not over k" contradicts the
      card's "need not be isomorphic as k-schemes" ($X = \PP^1$).
    - [x] D-IV2ETCOV: "proper nonempty open $U$" fails for clopen $U$; require $U$ not closed.
    - [x] D-MORLOCAL: the $\PP^1$ example shows non-locality for proper only; add the
      doubled-origin line for separated.
    - [x] F2, wiki link text that breaks the sentence (`[[ID]]` rendered as the card title
      inside prose): T-HARDLEF, T-COHSVAN, functors-and-topologies, FE-FULHIRZBUN,
      toric/polytopes-and-divisors, T-SRFZMT, T-CRVCM, T-CRVUNIF,
      P-AGXMISCTSENPONEBUNDLE steps 3, 4 (raw `\PP` visible), 8, D-CRVMOD, T-CRVJINV,
      PR-MORFINCHAR, P-AGXMISCOCONNECTED step 1, PR-IV2INSEP (two), resources exercise list.
      CONTRIBUTING (`XREF-1`) already requires explicit link text; the listed cards now carry it. The bare prose links in the rest of the corpus remain.
    - [x] F1, page prose restating a transcluded card: functors-and-topologies, blowups,
      affine-or-projective, dimension-and-degree, smooth-and-singular, projective-schemes,
      vanishing-and-duality, families, derived-functors-and-vanishing, toric/criteria,
      toric/affine-computations, the curves-and-surfaces pages, classes-of-morphism,
      fibres-and-images, finite-and-flat (PR-RJ3P7), smooth-unramified-etale.
    - [x] resources: bibliography key `[07]` has no author part.
      The bibliography is CSL YAML, and the Zotero item carries `citation-label: Har07`.
    - [x] P-AGXMISCTSENPONEBUNDLE statement "where the fibers smooth curves" lacks a verb;
      check the source first.
    - [x] toric/surfaces-and-morphisms: lead uses $u_i, b_i$, T-TORSURF uses $v_i, a_i$.
    - [x] Read P-AGH242AGREEDENSE and PR-QX0VL for a CARD-04 duplicate.
    **Acceptance:** each item read and repaired.

  Round 5 (revision `fe84046a76`, topology guide and early algebra) injected the node below;
  `audited-deployment` needs it.
  - **`ad5-topology-algebra`**. **Needs:** none.
    - [x] T-N6PYS: link text "topological embedding" targets D-9KQZT (Homeomorphism); target
      D-BCNUH.
    - [x] `[Lee13]` (T-N6PYS twice, D-UBWVX) and `[Munk84]` (D-RU2GC) render unlinked: no
      textbook collection or bibliography entry resolves them (CITE-1).
    - [x] Renderer: a citation with several keys (`[@Hat02; @Mun00]`, D-J6XOC, D-Z7I7F)
      renders as unlinked text; each key must link like a single-key citation.
    - [x] CARD-04: T-3X5FF and T-S5T5C both state Sylow's third theorem; merge, keep the
      T-3X5FF proof and the $n_p \le m$ remark, repoint L-WROBY.
    - [x] CARD-04: T-XDMK2 and T-3KCD6 are both "Cauchy's theorem"; merge and repoint.
    **Acceptance:** each item read and repaired. **Closed.**

  Round 5 (revision `fe84046a76`, collections) injected the node below; `audited-deployment`
  needs it.
  - **`ad5-collections`**. **Needs:** none.
    - [x] SRC-BERKELEY-PRELIM-SPRING-2021 9B lists P-BKS11-6B ($x^4+x+2011$); the 2021 paper
      asks $x^4+x+2021$. Give 9B its own card. Not a defect: a changed odd constant is a
      CARD-04 near-duplicate, and the P-BKS11-6B Variations remark states $x^4+x+2021$.
    - [x] SRC-UGA-PRELIM-FALL-2007 omits paper Problem 6; list P-F04T5 between P-5YTY5 and
      P-F07EX and fix the remark's problem count. The remark already counts the paper's seven problems.
    - [x] P-3AEDF: the Fall 2016 paper assumes $C^2$, the card (from Tie's list) $C^3$; keep
      the weaker hypothesis on the card and title (CARD-04).
    - [x] P-TKF72: the limit is over $R$, not $z$, and $R$ names two radii; follow the paper.
    - [x] P-AEWN6 part (1) lacks "Let"; P-57CAX part (2) has "Let Let".
    - [x] SRC-TEXT-FOL99: P-RVL3K part (a) is not Folland 6.7 (6.7 assumes
      $f \in L^p \cap L^\infty$ on any measure space); drop that appearance.
    - [x] SRC-TEXT-SS05: E-L3F4O asks more than SS III 1.1; locator "1.1 as part".
    **Acceptance:** each item read and repaired. **Closed.**

  Round 5 (revision `fe84046a76`, analysis guides) injected the node below;
  `audited-deployment` needs it.
  - **`ad5-analysis`**. **Needs:** none.
    - [x] PR-L35O7, case $p=\infty$: the exceptional set omits
      $\{\abs{f_{n_1}} > \norm{f_{n_1}}_\infty\}$, so "bounded" does not follow; add it.
    - [x] Renderer and CITE-1: a citation links only when a `SRC-TEXT-<key>` collection exists.
      [Foll13] (13 uses; the collection is SRC-TEXT-FOL99, a different edition), [Apos74],
      [Abbo16], [Ahlf79], [Har07], [Gath21], [PiAr12], [Lee13], [Munk84] render unlinked, and
      the site has no bibliography page. Every citation must resolve to a reader-facing target.
      Subsumes the multi-key item in `ad5-topology-algebra`.
    - [x] Check "[Ahlf79, Chapter 3, Section 3.2, Definition 12]" against the book. Correct:
      Ahlfors (1979), Ch. 3, \S 3.2 "The Cross Ratio", p. 78, Definition 12.
    **Acceptance:** each item read and repaired. **Closed.**

  - **`ad6-prelim`**. **Needs:** none. Round 6 at 1c16b39fdc; report in the session scratchpad r6-prelim.md.
    - [x] P-UGAP08F-04: the title carries a source locator (CARD-02); retitle by the mathematics.
    - [x] SRC-UGA-PRELIM-FALL-2008: the P-UGAP13F-06 comment says "repeated exactly", but 3(b) is worded differently.
    - [x] P-GB7EM: the solution structure breaks STYLE-08.
    - [x] SRC-BERKELEY-PRELIM-SPRING-2013: provenance is Sp13_Solutions.pdf. Keep it if that department PDF prints the problem statements; otherwise find the paper. Kept: the PDF prints every problem statement.
    - [x] P-BKF20-1B: the hint printed on the paper is missing.
    - [x] UGA Spring 2003 #1b and UGA Fall 2015 extractions lose text. MinerU Flash drops the same locations on every run; they are transcribed from page renders and noted in each extraction.
    - [x] UGA Fall 2015 P-5RZWO, P-MOL6S, P-TOIEK, P-3CU65: informal solutions with errors (S/A and f/g mismatches, "take ε→0", "(Maybe not necessary?)", a recurrence in place of a closed form) and "Goal" paragraphs; rewrite under STYLE-08.
    - [x] P-3CU65: the title claims more than the problem asks.
    **Acceptance:** each item read and repaired. **Closed.**

  - **`ad6-site`**. **Needs:** none. Round 6 at 1c16b39fdc; report in the session scratchpad r6-site.md.
    - [x] bibliography.html: [StSh03] labels both Stein–Shakarchi Complex Analysis and Fourier Analysis; give each a distinct citation label in Zotero and re-export.
    - [x] Bibliography title case: "hilbert spaces" (Stein–Shakarchi 2005), "Introduction to Commutative algebra", "Functions of One complex Variable I" and about four more; fix the titles at the Zotero source.
    - [x] Miranda dated 2025 (gsm/005 is 1995); Guillemin–Pollack dated 2025 (chel/370 is 2010); fix the dates in Zotero.
    - [x] Folland entry prints the publisher twice ("John Wiley & Sons, Incorporated, Wiley").
    - [x] bibliography.html entries are not in alphabetical order by author.
    - [x] P-MMAQ-TBOFU3T6VV: the title is a truncated sentence with a literal \textit; retitle by the mathematics.
    - [x] SRC-TOP-WORKSHOP: provenance chips show raw file names, including the typo "connnected".
    **Acceptance:** each item read and repaired. **Closed.** The sort lives in vocabularies/citation-style.csl, the CSL owner of bibliography order.

  - **`ad7-text`**. **Needs:** none. Round 7 at 3f0a38feb1; report in the session scratchpad r7-text.md.
    - [x] Zotero: Miranda title still lower case; [RBKG13] lists Bers as an author (authors are Rodríguez, Kra, Gilman); [Hart10] is the 1977 GTM 52; [Harr10] is the 1992 GTM 133; Munkres publishers carry catalogue residue ("Addison-Wesley publ", "Prentice Hall, Inc"). Fix in Zotero, re-sync, repoint changed keys.
    - [x] Zotero: the PDF FX65DFGE on Dummit–Foote A4FFDNKB is Herstein's Abstract Algebra; remove or replace that attachment.
    - [x] P-MMAQ-WV7QEYSPXM: hint typo `\sigma_{\varphi_1}(K)\inverseof{\sigma}` (should be $\sigma\varphi_1(K)\sigma^{-1}$) and "construcing"; SRC-TEXT-DF04 gives no exercise locator (5.5.6).
    - [x] SRC-TEXT-HUN74: 63 of 73 appearances have no exercise locator.
    - [x] SRC-TEXT-HAT02, SRC-TEXT-SS03: the pages show no exercise numbers; give each appearance its locator.
    - [x] E-SS1.EX-13: the statement never introduces Ω (the book: open set Ω; the solution assumes a region).
    - [x] E-SS4.EX-9: `z` and `S` outside math, the doubled comma in "closure of $S ,$ ,", and a leading "9." in the statement.
    **Acceptance:** each item read and repaired. **Closed.** The DF04, HUN74, HAT02 and SS03 appearances carry their book locators.

  - **`ad7-prelim`**. **Needs:** none. Round 7 at 3f0a38feb1; report in the session scratchpad r7-prelim.md.
    - [x] P-JHUSP01CAA: extraction residue in the statement ("Question 1.", trailing "·").
    - [x] P-UGAP13F-08: `1+\sqrt3,i` renders as "√3,i" in four places; write $1+\sqrt3\,i$.
    - [x] P-F04I9: the title "cannot compose" is false; the claim is that $f\circ g$ has no differentiable inverse.
    - [x] P-UCLAB10S-*: all 12 statements start with "Problem N." (CARD-02).
    - [x] Extractions with no provenance record: extracted/Spring88.md, Fall_2014_Exam.md, basic-10S.md, grad_prelim_Fall04.md, grad_prelim_Spring07.md. Regenerate with MinerU Flash and correct any location Flash drops from a page render, noting it in the file.
    - [x] P-BKS93-05: the solution answers "c ∈ R" from the zero solution only. Read the paper: if it asks for values of c admitting a nonzero solution, the answer is $c=\pm\sqrt{1-m^2/4k^2}$, $1\le m\le 2k-1$; write that.
    - [x] P-F04L8: the statement adds "oriented counterclockwise", which the paper does not print.
    **Acceptance:** each item read and repaired. **Closed.** The P-BKS93-05 paper asks for "a solution", so the literal answer stays; a remark solves the nonzero reading, with $1\le m\le 2k$ ($m=2k$ is $c=0$).

  - **`ad8-prelim`**. **Needs:** none. Round 8 at 4529fee3cb; report in the session scratchpad r8-prelim.md.
    - [x] P-F03P2: the paper's matrix is (1 2; 2/9 1); the card, title and solution use 1/2. Correct and re-solve.
    - [x] SRC-BERKELEY-PRELIM-SUMMER-1984 (all 20 cards) and SRC-BERKELEY-PRELIM-FALL-2016 (most cards): statements are untranscribed MinerU residue (lost arrows, \binom for a matrix, "C {0}", \boldsymbol). Transcribe each statement against the paper, one card at a time.
    - [x] P-IMYQU: the solution display drops its line breaks and is clipped; the integrals lack dx.
    - [x] P-SK4KT: a garbled sentence about the eigendecomposition in the solution.
    **Acceptance:** each item read and repaired. **Closed.** The extraction detector measured only Unicode glyphs outside dollar spans, so MinerU residue inside `$…$` passed; it now also measures MinerU-spaced LaTeX (`x ^ { 6 }`), which opens `mineru-spaced-statements`.

  - **`mineru-spaced-statements`**. **Needs:** none. `just extraction-detector` reports 1006 problem cards whose statements carry MinerU-spaced LaTeX (`^ { 6 }`, `\operatorname* { l i m }`), the residue that hid the ad8-prelim Summer 1984 and Fall 2016 defects. Transcribe each statement against its paper, one card at a time, by collection; the spacing alone is harmless, so read each for the lost operators, matrices and prose set in math that travel with it.
    **Acceptance:** the detector reports no `mineru-spaced` finding. **Closed.**

  - **`ad9-exams`**. **Needs:** none. Round 9 at 2cd9297bd3; report in the session scratchpad r9-exams.md.
    - [x] P-RASP23D: the solution says the Riesz measure is inner regular on every Borel set; it is not ($E=\RR\times\{0\}$, Rudin RCA 2.17). The answer is No.
    - [x] P-MMAQ-OXWRG3VWFJ (b): asks about intermediate groups; the source asks about intermediate fields of a Galois extension of degree 2009.
    - [x] SRC-UW-ALG-2009 and SRC-UW-ALGEBRA-2005-2018 section 2009: the paper has 8 problems; Problems 5 and 8 have no card. Add them.
    - [x] P-UCLARA13F-10: `\widehat f^{,2}` has a stray comma.
    - [x] P-UCLARA13F-04: lost the closed domain; $u$ is continuous on $\overline{\mathbb D}\setminus\{0\}$.
    - [x] P-UCLARA13F-01 … -06: classified real analysis; the paper marks Problems 1-6 complex analysis.
    - [x] P-CASP19G: stale parenthetical about ν in the solution.
    - [x] P-8XT86: the source's second norm |||·||| and the new norm on X are typeset as the original norm, so the statement reads as tautologies.
    - [x] P-NIC7C: λ: T(X)→ℂ; the exam's spaces are real.
    - [x] P-TOP-WORKSHOP-D4-03: "(Jan '04 # A3)" in the statement (CARD-02).
    - [x] Card pages list one collection twice when a card appears in two sections of it (P-TOP-WORKSHOP-D3-04, -D3-05); render one entry per appearance with its section name.
    **Acceptance:** each item read and repaired. **Closed.**

  - **`ad9-prelim`**. **Needs:** none. Round 9 at 2cd9297bd3; report in the session scratchpad r9-prelim.md.
    - [x] P-KU6C3: the bracketed note lost its opening, leaving a stray "]"; the source asks only for the root 1 and gives 1 (double) and −2 as information.
    - [x] P-HOBOM: malformed step numbering (two step 1s, a mid-proof QED, "Steps 1 and 1", duplicate anchors).
    - [x] P-UCLAB01F-06 step 1: unescaped set braces.
    - [x] P-UCLAB02W-09 step 2: doubled "+ ⋯ + +".
    - [x] P-UCLAB02F-08 step 5: `,qquad` missing its backslash.
    - [x] P-BERK77S-02 step 3: the triangle can touch the real axis; cite step 1 or 2, not Cauchy's theorem in an open half-plane.
    - [x] P-HUKW5: orphan justification fragments; the step 3.1 list collapsed inline.
    - [x] Summer77_extracted.md problem 20: "x_3 + - x_5"; the PDF prints "+".
    **Acceptance:** each item read and repaired. **Closed.**

  Content nodes (owner: the named cards and pages; one item at a time):
  - **`ad-algebra-content`**. **Needs:** none. CARD-04 merges confirmed in round 1
    (PR-U5CHT/FF-QVQXM, E-EMESP/E-P4LG6, D-FIB7S/FD-OR3BW, T-SVJUN/FT-7NMQR, E-DFUYC/E-R6I7G,
    T-4XKGD/L-6QBOJ, PR-GJLQP/P-5UUNM, T-GJNT5/C-HWX2P/E-NNTQB, P-AMD-QBEEJKCX/E-AMD-UEHZOJ3K);
    notation and structure defects in D-53LTN, PR-IOMVN, PR-SLWTB, T-WRMBM, PR-KGHJ2, E-P5BF6,
    the-class-equation, orbit-stabilizer, characteristic-subgroups, is-this-group-abelian.
    **Acceptance:** each item read and repaired. **Closed.** E-P5BF6 needed no card change: its
    split QED step is the `(e)` list defect owned by `ad-fancy-lists`.
  - **`ad-topology-ag-content`**. **Needs:** none. PR-QV4U5 proof does not prove its CW
    statement; C-ILVEB empty concept block; C-GJRYO dangling colon; T-BX4LD notation;
    E-JX67Q delimiters; separated-and-proper and curves-in-projective-space restatements;
    wiki/prelim/worked-exams/all.md stray remark. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-analysis-content`**. **Needs:** none. P-RAF23C step 2 fails for infinite measure;
    P-RAF23F/G titles carry TeX outside math; P-RAF23G "measurable space"; STYLE-05 part
    keying in P-SMK7Q, P-NYOLD, P-PEND3, P-7XPOK; GUIDE-REAL-ANALYSIS joint-exam intro
    describes complex analysis. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-public-notes`**. **Needs:** none. Curation notes on public pages
    (workshops-guide topology lede, SRC-RA-WORKSHOP remark) and RES-01 duplicate PDF links
    in wiki/prelim/resources/problems.md. **Acceptance:** each item read and repaired. **Closed.**
  - **`ad-prelim-resource-intake`**. **Needs:** none. `RES-02`: wiki/prelim/resources/problems.md
    links `assets/attachments/calculus_practice_test3.pdf`, which no collection lists as
    provenance. **Acceptance:** the PDF is ingested as a collection, like the GRE chapter
    reviews, and the page links that collection. **Closed:** ingested as `SRC-CALCULUS-PRACTICE-TEST3`.
  - **`ad-calcpt3-extraction`**. **Closed.** A per-page MinerU Flash extraction of
    calculus_practice_test3.pdf is checked in. Each `P-CALCPT3-*` card and each reused card
    was compared with it. Where they disagree (Questions 9, 11, 43, 44), the page render
    confirms the card.
  - **`ad-rasp22a-radon-restriction`**. **Needs:** none. P-RASP22A statement 3 (restriction
    $\mu_A$ of a Radon measure to an open set $A$): the written proof claims $\mu$ is inner
    regular on every Borel set, which fails for a non-$\sigma$-finite Radon measure, and it never
    proves outer regularity of $\mu_A$. Decide whether $\mu_A$ is Radon in general (the Riesz
    measure of $f\mapsto\int_A f\,d\mu$ agrees with $\mu_A$ on open sets and on subsets of $A$;
    the open question is the mass it gives to $\partial A$) and write a correct answer.
    **Acceptance:** the card states the correct truth value with a complete proof or counterexample.
  - **`ad-topf22h-cube-gluing`**. **Needs:** none. P-TOPF22H (UCSD Topology Fall 2022): the cube
    figure does not fix the face identifications. The P glyphs on the front and back faces are
    upright at diagonally opposite positions, the R on the right face is mirrored, and the two Q
    glyphs are vertical flips of each other. The written solution assumes P and Q are translations
    and R is a half-turn, which the figure does not support. Read the glyphs from the exam page,
    decide the gluing maps, and rewrite the statement and the solution.
    **Acceptance:** the card statement names each face map, and the solution computes the
    space for that gluing.
  - **`ad-ucsd-justin-missing-items`**. **Needs:** none. SRC-UCSD-TOP-JUSTIN lacks cards for
    items present in the sheet extractions: sheet 2 #11 (first half), sheet 4 #2-4 and #6-16,
    sheet 7 #9, sheet 11 #5, and sheet 13 #2-18. Sheets 5, 6 and 9 have no checked-in extraction.
    **Acceptance:** each listed item is a card in the collection in source order, and sheets 5,
    6 and 9 are extracted and compared with their cards.
  - **`ad-uga-ra05-complex-part`**. **Needs:** none. SRC-UGA-RA-SPRING-2005: the retained
    Combined_Analysis_Spring_2005.docx is one exam with a real-analysis part and a five-problem
    complex-analysis part, and the collection lists only the real part. Add the complex part as
    cards and as a second section of this collection, and classify the collection under both
    areas. **Acceptance:** the collection lists all ten problems in source order, in two sections.
  - **`ad-justin-band-figure`**. **Needs:** none. P-AMD-CM4OPBUE (sheet 3 #4): the left band
    figure appears to have interlinked bands, and the solution claims the surface is planar with
    boundary circles capped to give $S^2$. Read the figure from the page render, decide the
    surface, and rewrite the solution. **Acceptance:** the solution identifies each surface from
    the figure as drawn.
  - **`ad-unl-combinatorics-area`**. **Needs:** none. The Section A problems of the UNL
    850-871 and 852-871 qualifying exams (P-UNL850871-06A1 to 06A5, P-UNL850871-08A1 to 08A5,
    P-UNL852871-07A1 to 07A5, and the 852 or 850 parts of the other UNL combined exams) are
    combinatorics and graph theory: inclusion-exclusion, Erdős-Ko-Rado, Burnside counts, codes,
    trees, Ramsey. They carry `areas: [topology]` because the combined exam is filed as a
    topology collection. No registered area holds combinatorics. Decide whether these problems
    are in scope, and if so under which area. **Acceptance:** each listed card carries the
    decided area, or the decision to remove the Section A parts is applied to the collections.
  - **`ad-unsorted-duplicate-candidates`**. **Needs:** none. The reading of the UNSORTED buckets
    found these pairs that may state the same mathematics; each needs both cards read and, if
    the mathematics is the same, a `CARD-04` merge. Algebra: E-AMD-F5ZHMJNK / E-AMD-YBSKHIZ3(b);
    E-AMD-OFJC25BM / E-AMD-X26OEAAA; E-AMD-4TXVF5CA / E-AMD-TSKS3JTO; E-NXHG6 / P-2E7UB;
    P-AMD-QBEEJKCX / P-C2WAH; P-FINEA / P-KGXWN; P-JPTMN / P-KTQL5; P-GSJ2A / P-HH3JN;
    P-TA426(b) / P-WL4WF; P-TO7DK(d) / P-V23K4. Complex analysis: E-YEIQ5 / P-ALI5T;
    P-TFO34 / P-IOUZO(e); P-4JM4Y / P-4PTIX(a); E-Y22HZ / P-G2RYI; P-Y4TND / P-YWMCT. Real
    analysis and topology: P-2YFVO / E-Y4GZM, E-E4H2J, E-LYXHE, E-GQEMZ; P-4EOE5 / E-3OAGD,
    E-JJ746; P-FNUGX / E-TZFC7, E-7EL3U, E-UYQED; P-6BKXI / E-QCYEM, E-KUOXT; P-O2PWG /
    E-FFARP, E-4CL6A, E-SA3HI; P-PEND3 / E-XHB3F, E-CGVE4, E-BTA5L; E-IECHS / P-GAA3C.
    Elsewhere: P-G7GOP / P-XCE4G. **Acceptance:** each pair is merged or both cards are kept
    after reading.
  - **`ad-bkf93-12-contour`**. **Needs:** none. P-BKF93-12: the retained Fall93.pdf prints
    "../Fig/Pr/Fa93-12.ps not found" where the curve $\gamma$ should be, so the statement has no
    contour and the solution answers in terms of winding numbers. Find another copy of the Fall
    1993 Berkeley prelim (or the Fa93-12 figure) and transcribe the curve. **Acceptance:** the
    statement describes $\gamma$ as drawn and the solution gives a number.
  - **`ad-bks81-11-contour`**. **Needs:** none. P-BKS81-11: the retained Spring81.pdf prints
    "../Fig/Pr/Sp81-11.ps not found" where the curve $C$ should be, so the statement has no
    contour and the solution answers in terms of winding numbers. Find another copy of the Spring
    1981 Berkeley prelim (or the Sp81-11 figure) and transcribe the curve. **Acceptance:** the
    statement describes $C$ as drawn and the solution gives a number.
  - **`ad-bks83-4-network`**. **Needs:** none. P-BKS83-4: the retained Spring83.pdf prints
    "../Fig/Pr/Sp83-4.ps not found" where the triangular network should be, so the statement
    does not determine the network and the solution only shows the answer depends on it. Find
    another copy of the Spring 1983 Berkeley prelim (or the Sp83-4 figure) and transcribe the
    network. **Acceptance:** the statement describes the network as drawn and the solution names
    its symmetry group.

### Marking a node closed

When a node meets its acceptance, mark it closed in this file in the same delivery so it
cannot be selected again. A later regression is repaired at its current owner rather than by
replaying the historical node.

### Terminal nodes

These nodes run after `audited-deployment` closes. They are finite cleanup work, not a
recurring reporting programme.

- **`refactor-audit`**. **Needs:** `audited-deployment`.
  Inspect the tooling and site sources — `tools/`, `site/`, generators, and checkers, not authored mathematics — for concrete defects in ownership, encapsulation, duplicated sources of truth, unnecessary bespoke machinery, and maintainability that affects reliable behavior.
  Repair a defensible finding at its actual owner rather than creating an audit receipt, inventory-only node, or approval stage.
  A genuinely large cross-owner repair may become a concrete DAG node with its real dependencies and behavioral acceptance; the audit itself does not recursively manufacture scheduling nodes.
  **Acceptance:** every finding from the pass has been repaired at its owner, and a final repository-wide pass over the same scope finds no further concrete defect requiring work.

- **`type-paydown`**. **Needs:** `refactor-audit`. Repair the tooling type defects for which stronger typing materially improves legibility, comprehension, or static reasoning about correctness.
  The objective is the resulting program structure, not a diagnostic count.
  Do not add contortions whose only value is silencing a checker.
  **Acceptance:** the type defects selected by the refactor pass have been repaired at their owning interfaces, with behavior preserved and the resulting annotations/interfaces clearer than the state they replace.

- **`bloat-audit-loop`**. **Needs:** `type-paydown`.
  Make one final whole-tooling/site convergence pass using the relevant lenses already established for this repository: publisher/tool architecture, proof-bearing tests, API and type design, dependency/offload opportunities, duplicated sources of truth, dead compatibility bridges, generated-versus-authored boundaries, build/preview cost, and AI-slop patterns.
  Compare bespoke Markdown parsing/rendering against Pandoc and the existing Markdown toolchain before polishing local machinery that should disappear.
  Inspect representative public behavior; source-text churn is not acceptance evidence.
  Repair each defensible finding at its owner.
  **Acceptance:** all findings from the pass are repaired and a final pass across those lenses finds no further defensible change.

Live issue state is on [GitHub issues](https://github.com/dzackgarza/new-qual-site/issues).
Do not mirror it here.

## 7. Author solutions

Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

Every current `kind: problem` card has an authored `solution` section. A newly added problem
without a solution is new authoring work under this procedure.

The per-card tasks are `select:P-…`, `read:P-…`, `source-review:P-…`, `prove:P-…`,
`attach:P-…`, and `commit:P-…`, each keyed by the card ID; names in Needs refer to the same
card's instance, and `select` needs nothing. Returning to selection creates an instance for a
different card. Work one card at a time in source order; independent subject streams may work
on different cards in the one checkout, on `main`, under [`QUAL-09`](CONTRIBUTING.md#named-policies).

`source-review` applies when incorporating a source solution; an original proof has no source
solution to review. Source reading and review of the authored proof are required in either
case. An unfinished source correction needed by a proof precedes that card's proof.
