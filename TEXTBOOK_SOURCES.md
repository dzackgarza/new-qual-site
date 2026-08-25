# Textbook Sources

Each textbook cited in the corpus lives as a Zotero item with an associated PDF and
 MinerU extraction. The extraction markdown is the source text for reading exercises
and writing cards.

What each collection lists is owned by its collection card under `corpus/collections/`
(`SRC-TEXT-*`): `sections:` is the per-section problem list, `completion:` the
remaining-work signal.

## Extraction locations

All paths are under `/home/dzack/Zotero/storage/<attachment-key>/`.

| Textbook | Zotero key | Attachment key | Extraction file |
|---|---|---|---|
| Hoffman & Kunze, *Linear Algebra* (2nd ed., 1971) | `IHUJ2G7R` | `IH2WQFQC` | `local-write-api-1783268640255-IHUJ2G7R_extracted.md` |
| Dummit & Foote, *Abstract Algebra* (3rd ed., 2004) | `A4FFDNKB` | `XIINH8MK` | `local-write-api-1783380265761-A4FFDNKB_extracted.md` |
| Hungerford, *Algebra* (GTM 73, 1974) | `EW5CVTDL` | `D8B427XZ` | `local-write-api-1783337690991-EW5CVTDL_extracted.md` |
| Smith, *Algebra Course Notes* (843-1 through 845-3) | `LCYL45LE` | — | `assets/attachments/8000e.pdf` (vendored) |

## Hoffman & Kunze, *Linear Algebra*

**Collection card:** `SRC-TEXT-HK71`
**Extraction:** 39 sections with exercises in the MinerU file.

- [x] §1.2 — Systems of Linear Equations (8 exercises)
- [x] §1.3 — Matrices and Elementary Row Operations (8 exercises)
- [x] §1.4 — Row-Reduced Echelon Matrices (10 exercises)
- [x] §1.6 — Invertible Matrices (12 exercises)
- [x] §2.1 — Vector Spaces (7 exercises)
- [x] §2.2 — Subspaces (9 exercises)
- [x] §2.3 — Bases and Dimension (14 exercises)
- [x] §2.4 — Coordinates (7 exercises)
- [x] §2.6 — Computations Concerning Subspaces (7 exercises)
- [x] §3.1 — Linear Transformations (13 exercises)
- [x] §3.2 — The Algebra of Linear Transformations (12 exercises)
- [x] §3.3 — Isomorphism (7 exercises)
- [x] §3.4 — Representation of Transformations by Matrices (13 exercises)
- [x] §3.5 — Linear Functionals (17 exercises)
- [x] §3.6 — The Double Dual (3 exercises)
- [x] §3.7 — The Transpose of a Linear Transformation (8 exercises)
- [ ] §4.2 — The Algebra of Polynomials
- [ ] §4.3 — Lagrange Interpolation
- [ ] §4.4 — Polynomial Ideals
- [ ] §4.5 — The Prime Factorization
- [ ] §5.2 — Determinant Functions
- [ ] §5.3 — Permutations and the Uniqueness of the Determinant
- [ ] §5.4 — Additional Properties of Determinants
- [ ] §6.2 — Characteristic Values
- [ ] §6.3 — Annihilating Polynomials
- [ ] §6.4 — Invariant Subspaces
- [ ] §6.5 — Simultaneous Triangulation; Simultaneous Diagonalization
- [ ] §6.6 — Direct-Sum Decompositions
- [ ] §6.7 — Invariant Direct Sums
- [ ] §7.1 — Cyclic Subspaces and Annihilators
- [ ] §7.2 — Cyclic Decompositions and the Rational Form
- [ ] §7.3 — The Jordan Form
- [ ] §7.4 — Computation of Invariant Factors
- [ ] §7.5 — Summary; Semi-Simple Operators
- [ ] §8.2 — Inner Product Spaces
- [ ] §8.3 — Linear Functionals and Adjoints
- [ ] §8.4 — Unitary Operators
- [x] §9.2 — Forms on Inner Product Spaces
- [x] §9.3 — Positive Forms
- [x] §9.5 — Spectral Theory
- [x] §10.1 — Bilinear Forms
- [x] §10.2 — Symmetric Bilinear Forms
- [x] §10.3 — Skew-Symmetric Bilinear Forms
- [x] §10.4 — Groups Preserving Bilinear Forms

**Notes:**
- §§2.1, 3.1, 3.2, 3.5, 3.6 have exercises in the book but the MinerU extraction doesn't label them with an "Exercises" heading — exercises appear as inline numbered items at the end of the section text.
- The `sections:` list on `SRC-TEXT-HK71` is the authoritative record; this checklist is derived from it and lags behind it. The card currently holds all 47 sections with exercises (§§1.2–10.4), so `completion` here is `incomplete` only in the sense that the book's exercises are not all written as cards — every section that has exercises in the extraction is listed on the card.

## Dummit & Foote, *Abstract Algebra*

**Collection card:** `SRC-TEXT-DF04`
**Extraction:** Full book (10 chapters). Only §5.5 Exercise 6 has been written as a card.

- [x] §5.5 Exercise 6 — Semidirect product isomorphism (`P-MMAQ-WV7QEYSPXM`)
- [ ] Chapter 0 — Preliminaries (§§0.1–0.3)
- [ ] Chapter 1 — Group Theory (§§1.1–1.7)
- [ ] Chapter 2 — Subgroups (§§2.1–2.5)
- [ ] Chapter 3 — Quotient Groups and Homomorphisms (§§3.1–3.5)
- [ ] Chapter 4 — Group Actions (§§4.1–4.6)
- [ ] Chapter 5 — Direct and Semidirect Products (§§5.1–5.7, except §5.5 Ex. 6)
- [ ] Chapter 6 — Further Topics in Group Theory (§§6.1–6.5)
- [ ] Chapter 7 — Introduction to Module Theory (§§7.1–7.6)
- [ ] Chapter 8 — Vector Spaces (§§8.1–8.4)
- [ ] Chapter 9 — The Structure of Rings (§§9.1–9.6)
- [ ] Chapter 10 — Fields (§§10.1–10.6)
- [ ] Chapter 11 — Galois Theory (§§11.1–11.6)
- [ ] Chapter 12 — Commissativity and Class Equations (§§12.1–12.3)
- [ ] Chapter 13 — The Sylow Theorems (§§13.1–13.4)
- [ ] Chapter 14 — Applications of the Sylow Theorems (§§14.1–14.6)
- [ ] Chapters 15–18 — Further group theory topics
- [ ] Chapters 19–26 — Ring and module theory topics
- [ ] Chapters 27–32 — Commutative algebra and field theory topics
- [ ] Chapters 33–36 — Additional topics

**Notes:**
- Definition, theorem, and proposition cards that reference D&F sections are omitted from `sections:` (see the collection card's remark for the list).
- The extraction has two PDF children: `A4FFDNKB_extracted.md` (MinerU) and `Abstract_algebra_fulltext`.

## Hungerford, *Algebra*

**Collection card:** `SRC-TEXT-HUN74`
**Extraction:** Full book (Chapters I–VII plus Introduction). 67 problem cards across 25 sections.

- [x] I.6 — Semigroups, Monoids and Groups
- [x] I.9 — Free Groups, Free Products, and Generators and Relations
- [x] II.1 — The Structure of Groups
- [x] II.2 — The Action of a Group on a Set
- [x] II.4 — Categories: Products, Coproducts, and Free Objects
- [x] II.5 — Morphisms
- [x] II.6 — Products and Coproducts
- [x] II.7 — Categories and Functors
- [x] II.8 — Some Basic Categorical Concepts
- [ ] II.3 — Subgroups, Normal Subgroups, and Quotient Groups
- [ ] II.9 — Quotient Groups and Homomorphisms
- [ ] II.10 — The Isomorphism Theorems
- [ ] III.* — Rings (all sections)
- [x] IV.1 — Modules, Homomorphisms and Exact Sequences
- [x] IV.2 — Free Modules and Vector Spaces
- [x] IV.4 — Hom and Duality
- [x] IV.6 — Tensor Products
- [ ] IV.3 — The Free Module over a Principal Ideal Domain
- [ ] IV.5 — Modules over Principal Ideal Domains
- [ ] IV.7 — Exact Sequences
- [ ] IV.8 — Modules over a Principal Ideal Domain
- [ ] IV.9 — The Structure of a Module over a Principal Ideal Domain
- [ ] IV.10 — The Rational Canonical Form
- [ ] IV.11 — The Jordan Canonical Form
- [ ] IV.12 — The Tensor Algebra
- [x] V.1 — Field Extensions
- [x] V.3 — Classical Straightedge and Compass Constructions
- [x] V.4 — Splitting Fields
- [x] V.5 — Algebraic Closure
- [x] V.6 — Separable Extensions
- [x] V.8 — Finite Fields
- [x] V.9 — Cyclotomic Polynomials
- [ ] V.2 — The Algebraic Closure of a Field
- [ ] V.7 — Normal and Separable Extensions
- [ ] V.10 — Inseparable Extensions
- [ ] V.11 — Composite Fields and Splitting Fields
- [ ] V.12 — The Primitive Element Theorem
- [ ] VI.* — Galois Theory (all sections)
- [x] VII.1 — Introduction to Homological Algebra
- [x] VII.2 — Ext and Tor
- [x] VII.3 — The Koszul Complex
- [x] VII.4 — Homology of Groups
- [x] VII.5 — The Crossed Homomorphisms
- [ ] VII.6 — Group Extensions
- [ ] VII.7 — The Ext Functor
- [ ] VII.8 — The Tor Functor

**Notes:**
- Chapter III (Rings) and Chapter VI (Galois Theory) are entirely unextracted.

## Smith, *Algebra Course Notes*

**Collection card:** `SRC-TEXT-SMI`
**Extraction:** Vendored PDF (`assets/attachments/8000e.pdf`) with vendored MinerU pipeline extraction (`assets/attachments/8000e_extracted.md`). Not in Zotero by decision — the packet has no canonical citation info.

- [x] Abelian groups / generators for abelian groups — items 1–6 in cards (item 0 is a reading task)
- [x] Euclidean domains — all of 1–9 in cards
- [x] Finitely generated abelian groups and $k[X]$ modules — all of 1–4 in cards
- [x] Jordan forms — all of 1–4 in cards
- [x] Noetherian rings — all of 1–10 in cards
- [x] Normality and localization — all in cards (sheet items 3, 4, 5 share one card)
- [x] Sylow subgroups — all of 1–10 in cards
- [x] Cycles in $S(n)$ and commutators — all of 1–10 in cards
- [x] Galois groups — concrete problems in cards; the ten prelim pointers (UGA prelims 1997–2006) not yet represented
- [x] Fall 2006 midterm and final exam — all problems in cards

**Notes:**
- The hosted MinerU API failed repeatedly on this file; the extraction was produced by a local MinerU pipeline run.
- The separate 843–845 course notes are a different document not yet in the library.
