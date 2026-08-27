# Document queue A: Wiki files with `title="?"` (defect 3)

95 wiki files carry `:::{.proof title="?"}` (or `.example title="?"`) at HEAD.
The `?` renders as a literal title on the built page.
Fix: remove `title="?"`, leaving `:::{.proof}` or `:::{.example}`.

108 instances are already fixed in the uncommitted working tree (pure removal).
Commit that fix, then rebuild to verify.

## Algebra (19 files)

- [ ] wiki/10_Algebra/01_Groups/01_Groups_Basics.md
- [ ] wiki/10_Algebra/01_Groups/10_Actions.md
- [ ] wiki/10_Algebra/01_Groups/11_Groups_Counting_Actions.md
- [ ] wiki/10_Algebra/01_Groups/12_Sylow_Theorems.md
- [ ] wiki/10_Algebra/01_Groups/13_Groups_Classification.md
- [ ] wiki/10_Algebra/01_Groups/14_Groups_Series.md
- [ ] wiki/10_Algebra/02_Rings/20_Rings.md
- [ ] wiki/10_Algebra/03_Fields/30_Fields_General.md
- [ ] wiki/10_Algebra/03_Fields/35_Fields_Extensions.md
- [ ] wiki/10_Algebra/03_Fields/36_Galois_Theory_Computations.md
- [ ] wiki/10_Algebra/04_Modules/40_Modules.md
- [ ] wiki/10_Algebra/05_Linear_algebra/020_Undergrad.md
- [ ] wiki/10_Algebra/05_Linear_algebra/050_Polynomials.md
- [ ] wiki/10_Algebra/05_Linear_algebra/100_JCF.md
- [ ] wiki/10_Algebra/05_Linear_algebra/120_RCF.md
- [ ] wiki/10_Algebra/05_Linear_algebra/200_Diagonalization.md
- [ ] wiki/10_Algebra/05_Linear_algebra/50_Linear Algebra.md
- [ ] wiki/10_Algebra/05_Linear_algebra/520_Counterexamples.md
- [ ] wiki/10_Algebra/13_Appendices/9951 Appendix.md

## Real Analysis (20 files)

- [ ] wiki/20_Real_Analysis/01_Basics/05_Advice and Essentials.md
- [ ] wiki/20_Real_Analysis/01_Basics/20_Basics.md
- [ ] wiki/20_Real_Analysis/01_Basics/20_Sets.md
- [ ] wiki/20_Real_Analysis/01_Basics/30_Continuity.md
- [ ] wiki/20_Real_Analysis/01_Basics/30_Sequences_Series.md
- [ ] wiki/20_Real_Analysis/01_Basics/35_Differentiability.md
- [ ] wiki/20_Real_Analysis/01_Basics/50_Commuting_Limits.md
- [ ] wiki/20_Real_Analysis/01_Basics/60_Littlewood Principles.md
- [ ] wiki/20_Real_Analysis/01_Basics/90_Counterexamples.md
- [ ] wiki/20_Real_Analysis/02_Measure/00_Measure.md
- [ ] wiki/20_Real_Analysis/03_Integration/00_Integration.md
- [ ] wiki/20_Real_Analysis/03_Integration/010_Counterexamples.md
- [ ] wiki/20_Real_Analysis/03_Integration/10_L1.md
- [ ] wiki/20_Real_Analysis/03_Integration/Lp.md
- [ ] wiki/20_Real_Analysis/03_Integration/Techniques.md
- [ ] wiki/20_Real_Analysis/04_Fourier/00_Fourier.md
- [ ] wiki/20_Real_Analysis/05_Functional_analysis/50_Functional Analysis.md
- [ ] wiki/20_Real_Analysis/08_Quals/2021-10-30.md
- [ ] wiki/20_Real_Analysis/13_Appendices/9900_Appendix_Inequalities.md
- [ ] wiki/20_Real_Analysis/13_Appendices/9900_Undergrad_Appendix.md

## Complex Analysis (44 files)

- [ ] wiki/30_Complex_Analysis/01_Basics/000_Tips_Techs.md
- [ ] wiki/30_Complex_Analysis/01_Basics/001_Precalculus.md
- [ ] wiki/30_Complex_Analysis/01_Basics/005_Calculus_Preliminaries.md
- [ ] wiki/30_Complex_Analysis/01_Basics/050 Series Reference.md
- [ ] wiki/30_Complex_Analysis/01_Basics/060_Analyticity.md
- [ ] wiki/30_Complex_Analysis/01_Basics/061_Analytic_NT.md
- [ ] wiki/30_Complex_Analysis/01_Basics/100_Complex Arithmetic.md
- [ ] wiki/30_Complex_Analysis/01_Basics/110_Complex_Preliminaries.md
- [ ] wiki/30_Complex_Analysis/01_Basics/115_Complex Log.md
- [ ] wiki/30_Complex_Analysis/01_Basics/120_Holomorphy and Calculus.md
- [ ] wiki/30_Complex_Analysis/01_Basics/125_Harmonic Functions.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/010_Cauchy_Theorem.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/012_Cauchy Inequality.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/012 Cauchy Integral Formula.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/015 Mean Value Theorem.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/020 Liouville.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/030 Identity Principle.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/030_Schwarz.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/030_Schwarz reflection principle.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/050_Morera_Theorem.md
- [ ] wiki/30_Complex_Analysis/02_Cauchy/070 Maximum modulus principle.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/015_Singularities.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/015_Zeros and Poles.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/016_Counting_Zeros_and_Poles_ArgPrinciple_Rouche.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/020_Argument Principle.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/030_Rouche.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/040_MMP.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/040_Open Mapping.md
- [ ] wiki/30_Complex_Analysis/03_Zeros_and_poles/050_Meromorphic Functions.md
- [ ] wiki/30_Complex_Analysis/04_Residues/020_Residues.md
- [ ] wiki/30_Complex_Analysis/04_Residues/025 Residues for integrals.md
- [ ] wiki/30_Complex_Analysis/05_Conformal_maps/030_Conformal_Mapping.md
- [ ] wiki/30_Complex_Analysis/05_Conformal_maps/030_Conformal Map Theory and Background.md
- [ ] wiki/30_Complex_Analysis/05_Conformal_maps/035_Conformal_Exercises.md
- [ ] wiki/30_Complex_Analysis/06_Maps_of_the_disc/000 Automorphisms of the disc and plane.md
- [ ] wiki/30_Complex_Analysis/06_Maps_of_the_disc/060_Schwarz lemma.md
- [ ] wiki/30_Complex_Analysis/06_Maps_of_the_disc/090_Riemann Mapping.md
- [ ] wiki/30_Complex_Analysis/07_Omitted_values/020_Casorati-Weierstrass.md
- [ ] wiki/30_Complex_Analysis/07_Omitted_values/050_Montel.md
- [ ] wiki/30_Complex_Analysis/07_Omitted_values/070_Picard.md
- [ ] wiki/30_Complex_Analysis/13_Appendices/090_Appendix FTA Proofs.md
- [ ] wiki/30_Complex_Analysis/13_Appendices/091_Appendix Unsorted.md
- [ ] wiki/30_Complex_Analysis/13_Appendices/PDEs.md
- [ ] wiki/30_Complex_Analysis/13_Appendices/Special Functions.md

## Topology (12 files)

- [ ] wiki/40_Topology/00_Basics/000_Preface.md
- [ ] wiki/40_Topology/01_Examples/202_Examples.md
- [ ] wiki/40_Topology/02_Point_set/001_Definitions.md
- [ ] wiki/40_Topology/02_Point_set/001_Examples.md
- [ ] wiki/40_Topology/02_Point_set/100_Point_Set.md
- [ ] wiki/40_Topology/03_Fundamental_group/202_Fundamental Group.md
- [ ] wiki/40_Topology/03_Fundamental_group/220_Covering_Spaces.md
- [ ] wiki/40_Topology/03_Fundamental_group/225_CW_Complexes.md
- [ ] wiki/40_Topology/04_Homology/230_Homology.md
- [ ] wiki/40_Topology/04_Homology/298_Appendix_Homological_Algebra.md
- [ ] wiki/40_Topology/05_Degree/240_Fixed_Points_and_Degree.md
- [ ] wiki/40_Topology/06_Manifolds/250_Surfaces_Manifolds.md