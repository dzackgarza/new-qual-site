# Document queue F: Wiki doctor findings

Source: `just doctor`, against 367 wiki pages.

The wiki is an authored study guide; see `AGENTS.md`, "The wiki is a textbook".
A checker measures the file, never the exposition.

## Defects

### order-at-least-100001 (44)

Pages with no position in their folder. `100001` is the marker an importer left; the page needs the position its author would give it.

- [ ] wiki/Algebra/Exercises/PSets/Final/AlgebraFinal.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 10/PSet 10 Quals.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 10/PSet 10.md: order 100002
- [ ] wiki/Algebra/Exercises/PSets/PSet 6/PSet6.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 7/PSet7.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 7/QualProblems.md: order 100002
- [ ] wiki/Algebra/Exercises/PSets/PSet 8/PSet8.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 9/PSet9.md: order 100001
- [ ] wiki/Algebra/Exercises/PSets/PSet 9/Quals.md: order 100002
- [ ] wiki/Algebra/Review/Algebra Fields Review 1.md: order 100001
- [ ] wiki/Algebra/Workshops/Algebra Week 1 Groups Warmup.md: order 100001
- [ ] wiki/Algebra/Workshops/Algebra Week 2 Finite Group Theory.md: order 100002
- [ ] wiki/Algebra/Workshops/Algebra Week 3 Sylow Theory.md: order 100003
- [ ] wiki/Algebra/Workshops/Algebra Week 4 Rings.md: order 100004
- [ ] wiki/Algebra/Workshops/Algebra Week n Rep Theory.md: order 100005
- [ ] wiki/Algebra/Workshops/Algebra Week n+1 Linear Algebra.md: order 100006
- [ ] wiki/Complex_Analysis/Appendices/Gauss-Lucas Theorem.md: order 100001
- [ ] wiki/Complex_Analysis/Appendices/Hurwitz.md: order 100002
- [ ] wiki/Complex_Analysis/Appendices/PDEs.md: order 100003
- [ ] wiki/Complex_Analysis/Appendices/Special Functions.md: order 100004
- [ ] wiki/Complex_Analysis/Workshops/Complex Week 1 Preliminaries.md: order 100001
- [ ] wiki/Complex_Analysis/Workshops/Complex Week 2 Cauchy.md: order 100002
- [ ] wiki/Prelim/Prelim Resources.md: order 100002
- [ ] wiki/Prelim/Problems/Berkeley Prelims.md: order 100001
- [ ] wiki/Prelim/Problems/Integral Practice.md: order 100002
- [ ] wiki/Prelim/Problems/UCLA Prelims.md: order 100003
- [ ] wiki/Prelim/Useful Tricks.md: order 100003
- [ ] wiki/Prelim/Worked_Exams/All.md: order 100001
- [ ] wiki/Real_Analysis/Basics/Integrability.md: order 100001
- [ ] wiki/Real_Analysis/Exercises/PSet 5.md: order 100001
- [ ] wiki/Real_Analysis/Exercises/PSet 6.md: order 100002
- [ ] wiki/Real_Analysis/Exercises/PSet 7.md: order 100003
- [ ] wiki/Real_Analysis/Exercises/PSet 8.md: order 100004
- [ ] wiki/Real_Analysis/Integration/Fubini.md: order 100001
- [ ] wiki/Real_Analysis/Integration/Lp.md: order 100002
- [ ] wiki/Real_Analysis/Integration/Techniques.md: order 100003
- [ ] wiki/Real_Analysis/Resources/Extra_Questions.md: order 100001
- [ ] wiki/Real_Analysis/Workshops/Real Week 1 Preliminaries.md: order 100001
- [ ] wiki/Real_Analysis/Workshops/Real Week 2 Measure Theory.md: order 100002
- [ ] wiki/Topology/Quals/UCSD/Quals/Old/Fall 2014.md: order 100001
- [ ] wiki/Topology/Quals/UCSD/Quals/Old/Final Fall 2017.md: order 100002
- [ ] wiki/Topology/Quals/UCSD/Quals/Old/Summer 2003.md: order 100003
- [ ] wiki/Topology/Quals/UCSD/Quals/Topology Problems (Solutions).md: order 100001
- [ ] wiki/Topology/Workshops/Topology Week 1 Preliminaries.md: order 100001

### obsidian-embed-syntax (9)

Obsidian `![[...]]` embeds, which Pandoc reads as literal text.

- [ ] wiki/Algebra/Workshops/Algebra Week 2 Finite Group Theory.md
- [ ] wiki/Algebra/Workshops/Algebra Week 4 Rings.md
- [ ] wiki/Algebra/Workshops/Algebra Week n+1 Linear Algebra.md
- [ ] wiki/Complex_Analysis/Cauchy/Identity Principle.md
- [ ] wiki/Complex_Analysis/Workshops/Complex Week 2 Cauchy.md
- [ ] wiki/Complex_Analysis/Zeros_and_poles/Singularities.md
- [ ] wiki/Prelim/Useful Tricks.md
- [ ] wiki/Real_Analysis/Resources/Problems.md
- [ ] wiki/Real_Analysis/Resources/Solutions.md

### task-list-item-lines (5)

Reading-progress checkboxes published as reader copy.

- [ ] wiki/Algebra/Resources/Problems.md: 2
- [ ] wiki/Complex_Analysis/Resources/Problems.md: 12
- [ ] wiki/Complex_Analysis/Resources/Solutions.md: 45
- [ ] wiki/Prelim/Prelim Resources.md: 41
- [ ] wiki/Real_Analysis/Resources/Problems.md: 12

### hash-todo-markers (0)

`#todo` markers published as reader copy.

ok

### tags-colon-lines (0)

Obsidian `tags:` lines published as reader copy.

ok

### hash-resources-only-lines (0)

Bare `#resources` tag lines published as reader copy.

ok

### notion-so-or-notion-site-urls (0)

Links into a Notion workspace no reader can open.

ok

### empty-bodies (0)

Pages with no body.

ok

### unreadable-wiki-pages (0)

Pages the reader cannot parse.

ok

## Measurements

### one-markdown-child-directories (15)

Folders holding one page besides the index.

- wiki/Algebra/Appendices (index.md + Appendix.md)
- wiki/Algebra/Exercises/PSets/Final (index.md + AlgebraFinal.md)
- wiki/Algebra/Exercises/PSets/Midterm (index.md + Midterm.md)
- wiki/Algebra/Exercises/PSets/PSet 6 (index.md + PSet6.md)
- wiki/Algebra/Exercises/PSets/PSet 8 (index.md + PSet8.md)
- wiki/Algebra/Review (index.md + Algebra Fields Review 1.md)
- wiki/Applied_Algebra/Resources (index.md + Source_Archive.md)
- wiki/Complex_Analysis/Exercises (index.md + Extra Questions.md)
- wiki/Real_Analysis/Functional_analysis (index.md + Functional Analysis.md)
- wiki/Topology/Basics (index.md + Preface.md)
- wiki/Topology/Degree (index.md + Fixed_Points_and_Degree.md)
- wiki/Topology/Examples (index.md + Examples.md)
- wiki/Topology/Exercises (index.md + Extra_Problems_AT.md)
- wiki/Topology/Manifolds (index.md + Surfaces_Manifolds.md)
- wiki/Topology/Workshops (index.md + Topology Week 1 Preliminaries.md)

### sibling-duplicate-titles (1)

Pages in one folder sharing a title.

- wiki/Complex_Analysis/Residues: title 'Residues' on Residues.md, index.md

### heading-or-wikilink-only-bodies (60)

Pages whose every line is a heading or a wikilink. These retype card data; TODO.md section 11 owns them.

- wiki/Algebra/Exercises/PSets/Final/AlgebraFinal.md
- wiki/Algebra/Exercises/PSets/Midterm/Midterm.md
- wiki/Algebra/Exercises/PSets/PSet 10/PSet 10 Quals.md
- wiki/Algebra/Exercises/PSets/PSet 6/PSet6.md
- wiki/Algebra/Exercises/PSets/PSet 7/PSet7.md
- wiki/Algebra/Linear_algebra/Enumerating.md
- wiki/Algebra/Linear_algebra/Exercises.md
- wiki/Algebra/Linear_algebra/Matrix_Groups.md
- wiki/Algebra/Quals/2021_Fall.md
- wiki/Algebra/Quals/Classification.md
- wiki/Algebra/Quals/Commutative Algebra.md
- wiki/Algebra/Quals/Extra Problems Commutative Algebra.md
- wiki/Algebra/Quals/Extra Problems Linear Algebra.md
- wiki/Algebra/Quals/Fields and Galois Theory.md
- wiki/Algebra/Quals/Group Actions.md
- wiki/Algebra/Quals/Linear Algebra.md
- wiki/Algebra/Quals/Linear Algebra_JCF.md
- wiki/Algebra/Quals/Modules.md
- wiki/Algebra/Quals/Simple Solvable.md
- wiki/Algebra/Quals/Sylow Theory.md
- wiki/Algebra/Representation_theory/Representation_Theory.md
- wiki/Complex_Analysis/Appendices/Gauss-Lucas Theorem.md
- wiki/Complex_Analysis/Basics/Basics_Exercises.md
- wiki/Complex_Analysis/Quals/1_Maps_of_Disc.md
- wiki/Complex_Analysis/Quals/2021_Fall.md
- wiki/Complex_Analysis/Quals/Argument Principle.md
- wiki/Complex_Analysis/Quals/Continuity.md
- wiki/Complex_Analysis/Quals/IntegralsCauchy.md
- wiki/Complex_Analysis/Quals/Laurent Expansions.md
- wiki/Complex_Analysis/Quals/Laurent_Singularities.md
- wiki/Complex_Analysis/Quals/Liouville_PowerSeries.md
- wiki/Complex_Analysis/Quals/Residues.md
- wiki/Complex_Analysis/Quals/Riemann Mapping and Casorati.md
- wiki/Complex_Analysis/Quals/Rouche 8155h.md
- wiki/Complex_Analysis/Quals/Schwarz Reflection.md
- wiki/Complex_Analysis/Quals/Schwarz.md
- wiki/Prelim/Useful Tricks.md
- wiki/Real_Analysis/Basics/Integrability.md
- wiki/Real_Analysis/Measure/Exercises.md
- wiki/Real_Analysis/Quals/01_2014_Fall_Exam2.md
- wiki/Real_Analysis/Quals/01_2018_Fall_Exam1.md
- wiki/Real_Analysis/Quals/01_2018_Fall_Exam2.md
- wiki/Real_Analysis/Quals/10_2019_Fall_Exam1.md
- wiki/Real_Analysis/Quals/10_2019_Fall_PracticeExam2.md
- wiki/Real_Analysis/Quals/2021_Fall.md
- wiki/Real_Analysis/Quals/Extra.md
- wiki/Real_Analysis/Quals/Extra_Problems.md
- wiki/Real_Analysis/Quals/Integration Fubini Tonelli.md
- wiki/Topology/Quals/UCSD/Quals/Old/Fall 2014.md
- wiki/Topology/Quals/UCSD/Quals/Old/Final Fall 2017.md
- wiki/Topology/Quals/UCSD/Quals/Old/Summer 2003.md
- wiki/Topology/Quals/UCSD/UCSD_Fall 2014.md
- wiki/Topology/Quals/UCSD/UCSD_Summer 2003.md
- wiki/Topology/Quals/UGA/Cell Complexes and Attaching Maps.md
- wiki/Topology/Quals/UGA/Covering Spaces.md
- wiki/Topology/Quals/UGA/Fixed Points.md
- wiki/Topology/Quals/UGA/Fundamental Group.md
- wiki/Topology/Quals/UGA/Homology and Degree Theory.md
- wiki/Topology/Quals/UGA/Misc.md
- wiki/Topology/Quals/UGA/Surfaces.md
