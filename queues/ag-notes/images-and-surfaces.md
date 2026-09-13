# Images and Hartshorne V

## Hartshorne V

Targets in this section are under `corpus/collections/SRC-TEXT-HART77/`. Exercise numbers refer to the source page, not a count inferred from the collection index.
The source statements, subparts, hints and footnotes were compared with the target bodies.
The source pages have no hidden solution text in `title` attributes.

| Source | Status | Target and remaining work |
| --- | --- | --- |
| `Hartshorne/5_Hartshorne/5_1x.html` | migrated | V.1.1–12: `P-AGH511EULERCHAR`, `P-AGH512HILBPOLY`, `P-AGH513VIRTGENUS`, `P-AGH514LINEONSURF`, `P-AGH515KSQUARED`, `P-AGH516DIAGONAL`, `P-AGH517ALGEQUIV`, `P-AGH518COHOMCLASS`, `P-AGH519HODGEINDEX`, `P-AGH5110WEILRH`, `P-AGH5111FINITEAUT`, `P-AGH5112NUMAMPLE`. The algebraic-equivalence footnotes, divisor-class pairing hint, Castelnuovo–Severi hint, and finite-class argument are present. |
| `Hartshorne/5_Hartshorne/5_2x.html` | partial | V.2.1–17 statements, subparts and footnotes survive in `P-AGH521BASEUNIQUE` through the source-ordered V.2 entries ending `P-AGH5217CONORMALSPLIT`. This includes stability, characteristic-p examples, all ruled-surface inequalities and the characteristic-dependent conormal answer. Restore the source star on V.2.17 in its collection appearance. |
| `Hartshorne/5_Hartshorne/5_3x.html` | migrated | V.3.1–8: `P-AGH531PABLOWUP`, `P-AGH532MULTINTER`, `P-AGH533AMPLEPULLBACK`, `P-AGH534MULTLOCRING`, `P-AGH535HYPERELLGENUS`, `P-AGH536ANALYTICEQUIV`, `P-AGH537EMBRESOLUTION`, `P-AGH538INEQUIVSING`. Includes infinitely near intersection points, Hilbert–Samuel definitions/hints, and every displayed singularity equation. |
| `Hartshorne/5_Hartshorne/5_4x.html` | partial | V.4.1–16 text and hints survive in source order from `P-AGH541CONICSQUADRIC` to `P-AGH5416FERMATCUBIC`. Recover the Pascal picture for `P-AGH545PASCAL` and the Dynkin diagrams for `P-AGH5411WEYLGROUPS` from the detached figures below. The target substitutes the name of the E6 diagram for its actual graph. Restore the star on V.4.8 and starred subparts V.4.11(c), V.4.15(e). |
| `Hartshorne/5_Hartshorne/5_5x.html` | partial | V.5.1–8 statements and hints survive in `P-AGH551RESOLVERATFN` through `P-AGH558E8SINGULARITY`. The E8 incidence graph is missing from the last card; the detached source figure below supplies it. The reference to Fig. 23 in V.5.5 has no corresponding image in this deployed directory: recover the elementary-transformation figure from the textbook if it is needed for the hint. |
| `Hartshorne/5_Hartshorne/5_6x.html` | migrated | `P-AGH561COMPLETEINT` and `P-AGH562CHERNGRIFFITHS` preserve both statements and the Clifford/Riemann–Roch/Kodaira hint. |
| `Hartshorne/5_Hartshorne.html`; `Hartshorne/5_Hartshorne/5_1.html`, `5_2.html`, `5_3.html`, `5_4.html`, `5_5.html`, `5_6.html` | reference-only | Child-page navigation or a section heading only. The exercise pages above own the mathematical text. |
| `Hartshorne/5_Hartshorne/figures/2022-10-22_21-13-10.png` | partial | Readable Pascal configuration: six conic points, intersection points P,Q,R and their line. The statement survives in `P-AGH545PASCAL`; its diagram does not. |
| `Hartshorne/5_Hartshorne/figures/2022-10-22_21-16-28.png` | partial | Readable chain Dynkin diagram for V.4.11(a). `P-AGH5411WEYLGROUPS` preserves the chain description but not the figure. |
| `Hartshorne/5_Hartshorne/figures/2022-10-22_21-17-05.png` | partial | Readable E6 graph, central vertex of the five-vertex chain with one branch. Restore on `P-AGH5411WEYLGROUPS`. |
| `Hartshorne/5_Hartshorne/figures/2022-10-22_21-57-34.png` | partial | Readable E8 graph, seven-vertex chain with a branch at the third vertex from one end. Restore on `P-AGH558E8SINGULARITY`. |

## Study-guide image content

Image names below are relative to `attachments/`. The source-path inventory records their byte-identical aliases.
These rows concern the mathematics read in the images, not the presence of an image file in the target.

| Source image | Status | Target and remaining work |
| --- | --- | --- |
| `2022-01-09_12-23-25.png` | partial | `T-YYLPH` retains Hilbert's basis theorem and the polynomial-ideal consequence. `D-MORFIN` uses finitely generated modules but does not give the source's explicit definition for an arbitrary module by a finite generating list. Preserve that definition, rather than substituting the definition of a finite morphism. |
| `Pasted image 20220921202350.png` | partial | `D-MODCONORM` retains the determinant normal-bundle adjunction formula as well as divisor adjunction. Correct the base of its tensor product: restrict omega_X to Z before tensoring with the normal determinant, which is already an O_Z-module. |
| `Pasted image 20220921204544.png` | migrated | `T-MWDVL` and `T-COHRRS` retain curve Riemann–Roch in h0-h1 form; `T-COHFIN` retains vanishing above the dimension. |
| `Pasted image 20220315152915.png` | partial | Four sheaf operations. `wiki/algebraic-geometry/sheaves-of-modules/operations.md` changes the setting to sheaves of sets while claiming unsupported adjunctions for f! and f^!. Specify the sheaf category and map hypotheses before retaining these formulas. |
| `Pasted image 20220315153140.png`; `Pasted image 20220315153154.png` | partial | The double cover of the circle example survives in `FE-SHFISOSTALKS`, including the source error. Its pushforward constant sheaf is locally constant, though generally not constant. Use a specified coefficient group such as Z for the stalk/global-section comparison; arbitrary nonzero groups need not differ from their square. |
| `Pasted image 20220921204101.png` | partial | `T-TORDIV` has K=-sum D and the projective-space specialization. Restore the proof using the invariant logarithmic top form, a toric chart A1 times a torus, and a simple pole along each boundary divisor. |
| `Pasted image 20220921204305.png` | migrated | `T-DIVMAPPN` retains the linear-system map to projective space dual to the space of sections. The source's personal uncertainty is not mathematical content to publish. |
| `Pasted image 20220921204126.png` | migrated | `T-SRFADJ` retains the plane-curve genus calculation by adjunction. |
| `Pasted image 20220921204448.png` | partial | `T-COHSD` retains the pairing and Euler-characteristic symmetry but narrows proper nonsingular varieties to projective varieties. Restore the source's proper scope with the correct duality hypotheses. Its added singular-case remark also needs the Cohen–Macaulay restriction identified in the Definitions row. |
| `2022-01-09_12-22-51.png` | migrated | `T-MORZMT` retains connected fibers and purity of the exceptional locus over a smooth target. |
| `2022-01-09_12-23-55.png` | partial | `T-MORFIBDIM` preserves finite Noether normalization by linear projection. Make the infinite-field hypothesis explicit for this linear form. |
| `2022-01-09_12-24-40.png` | partial | `T-MORFIBDIM` preserves the projective-center dimension calculation. `D-QJ5M9` repeats the source's tautological statement as the normalization universal property. Replace it with the actual factorization for dominant maps from normal varieties, with direction and hypotheses stated. |
| `2022-01-09_12-28-49.png` | partial | `T-MORSTEIN` retains Stein factorization. Correct its extra claim equating a finite fiber's degree with its number of connected components; lengths and geometric points differ. |
| `2022-01-09_12-58-27.png` | partial | `T-SRFZMT` retains the common-resolution diagram. State the characteristic-zero hypothesis for its general-dimensional Hironaka assertion. |
| `2022-01-09_12-59-50.png` | partial | `T-SRFCAST` narrows the source contraction criterion from smooth algebraic surfaces to projective surfaces. Restore the intended scope and both directions. Its claim about infinitely many exceptional curves after blowing up arbitrary points also needs the source's general-position hypotheses; compare V.4.15. |
| `2022-01-09_13-01-09.png` | migrated | `T-SRFZMT` and `T-SRFCAST` retain factorization of surface birational morphisms and maps into point blowups and contractions. |
| `2022-01-09_13-03-01.png` | migrated | `FE-SRFBLOW` retains resolution, preservation of the smooth locus, simple normal crossings, embedded resolution and smooth blowup centers. |
| `2022-01-09_13-03-12.png` | migrated | `T-SRFKOD` retains the alternating normalization and point-blowup construction for surfaces. |
| `2022-01-09_13-03-27.png` | migrated | `T-SRFKOD` retains the minimal resolution and its factorization property. |
| `2022-01-09_13-06-25.png` | migrated | `T-MWDVL` retains the curve Riemann–Roch formulas. |
| `2022-01-09_13-07-04.png` | migrated | `T-SRFADJ` retains divisor adjunction and the surface numerical formula. |
| `2022-01-09_13-07-48.png` | partial | `D-CRVPLSING` gives the delta-invariant formula for plane curves; `FE-SRFBLOW` gives the genus drop under a blowup. Clarify that the source sum of m(m-1)/2 must include infinitely near singularities, unless the singularities are ordinary. |
| `2022-01-09_13-08-23.png` | migrated | `T-COHRRS` and `D-COHEULER` retain surface Riemann–Roch and the holomorphic Euler characteristic. |
| `2022-01-09_13-20-16.png` | partial | `T-SRFKOD` retains the classification via the twelfth plurigenus. State the complex/characteristic-zero setting of this classification rather than extending it without hypotheses. |

## Syllabi and reference attachments

The syllabus crops were read as topic lists, not as unwritten theorem proofs.
A named topic does not create an obligation to invent a chapter during migration.
Preserve their reading-list role separately from the private study plans that embed them.

| Source, relative to `attachments/` | Status | Disposition |
| --- | --- | --- |
| `Pasted image 20220517141232.png` | reference-only | Classical algebraic geometry syllabus: varieties, Grassmannians, dimension/degree, Chow varieties, Hilbert schemes and curves; Shafarevich/Harris reading pointers. |
| `Pasted image 20220517142058.png` | reference-only | Schemes/cohomology/curves syllabus with Hartshorne chapter-section reading ranges. |
| `Pasted image 20220517142240.png` | reference-only | Schemes and the opening cohomology syllabus, including derived functors and affine vanishing. |
| `Pasted image 20220517142250.png` | reference-only | Continuation: Cech/projective cohomology, Ext and duality. The lower edge is cropped; it is not evidence of further readable requirements. |
| `Pasted image 20220517142303.png` | reference-only | Schemes, formal schemes and cohomology syllabus. |
| `Pasted image 20220517142338.png` | reference-only | Complex surfaces syllabus: K3 periods, ADE quotients, resolution, Enriques classification and Bogomolov–Miyaoka–Yau. |
| `Pasted image 20220517142403.png` | reference-only | Toric syllabus through Stanley–Reisner relations and self-intersection. |
| `Pasted image 20220517142548.png`; `Pasted image 20221012003451.png` | reference-only | Complex geometry, Hodge/Lefschetz decomposition, Abel–Jacobi and de Rham/Dolbeault cohomology. The October crop also includes the Griffiths–Harris and Miranda text names. |
| `Pasted image 20220517142612.png`; `Pasted image 20221012002702.png` | reference-only | Algebraic geometry exam scope through curves, Riemann–Roch and Abel–Jacobi. Both readable lists were compared; the lower edge of the October crop starts another subject. |
| `Andrew Egbert.pdf`, `Bryden R Cais.pdf`, `Chris Lomont.pdf`, `ismail saglam and Chris.pdf`, `Jinhyun Park.pdf`, `Joe Cutrone and Nick Marshburn.pdf`, `Richard Borcherds.pdf`, `Steven V Sam.pdf`, `W Stein.pdf` | reference-only | Each entire PDF is byte-identical to the same filename in `assets/algebraic-geometry/resources/`, linked from the resources page. Their role is external solution material. This proves retention of the documents, not that each argument is correct or transcribed into a solution card. |
| `Kawamata Intro MMP.pdf`, `Algebraic Geometry All Tripos.pdf`, `iag.pdf`, `2013SP_algebra.pdf` | reference-only | Each entire PDF is byte-identical to the same filename in `assets/algebraic-geometry/resources/`, linked from the resources page. Retained reference documents; extracting every contained exercise is a separate source-intake task, not evidence required to establish that these documents survived. |
| `Bryden R Cais.pdf.png`, `Bryden R Cais.pdf_1.png`, `Richard Borcherds.pdf_1.png`, `Chris Lomont.pdf_1.png`, `ismail saglam and Chris.pdf_1.png`, `Jinhyun Park.pdf_1.png` | reference-only | Small first-page previews of the retained PDFs. They supply no source version beyond those complete documents. |
