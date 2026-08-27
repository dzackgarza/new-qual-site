# Document queue B: Wiki files with naked URLs (defect 16)

17 wiki files have bare `<https://...>` URLs as link text, which overflow the column on mobile.
Fix: convert to `[link text](url)` markdown links.

161 URL conversions are already done in the uncommitted working tree.
Commit that fix, then rebuild to verify.

- [ ] wiki/10_Algebra/01_Groups/12_Sylow_Theorems.md
- [ ] wiki/10_Algebra/01_Groups/13_Groups_Classification.md
- [ ] wiki/10_Algebra/03_Fields/35_Fields_Extensions.md
- [ ] wiki/10_Algebra/03_Fields/36_Galois_Theory_Computations.md
- [ ] wiki/10_Algebra/05_Linear_algebra/100_JCF.md
- [ ] wiki/10_Algebra/08_Quals/200_Extra.md
- [ ] wiki/10_Algebra/11_Resources/000_Resources.md
- [ ] wiki/20_Real_Analysis/03_Integration/10_L1.md
- [ ] wiki/20_Real_Analysis/04_Fourier/00_Fourier.md
- [ ] wiki/30_Complex_Analysis/01_Basics/000_Tips_Techs.md
- [ ] wiki/30_Complex_Analysis/01_Basics/061_Analytic_NT.md
- [ ] wiki/30_Complex_Analysis/01_Basics/110_Complex_Preliminaries.md
- [ ] wiki/30_Complex_Analysis/04_Residues/020_Residues.md
- [ ] wiki/30_Complex_Analysis/05_Conformal_maps/031_Conformal_Standard.md
- [ ] wiki/40_Topology/03_Fundamental_group/220_Covering_Spaces.md
- [ ] wiki/40_Topology/11_Resources/20_Problems.md
- [ ] wiki/90_Archives/110_Further Studying.md