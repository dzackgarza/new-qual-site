# Textbook Sources

Each textbook cited in the corpus lives as a Zotero item with an associated PDF and
 MinerU extraction. The extraction markdown is the source text for reading exercises
and writing cards.

What each collection lists is owned by its collection card under `corpus/occurrences/`
(`SRC-TEXT-*`): `sections:` is the per-section problem list, `completion:` the
remaining-work signal.

## Extraction locations

All paths are under `/home/dzack/Zotero/storage/<attachment-key>/`.

| Textbook | Zotero key | Attachment key | Extraction file | Status |
|---|---|---|---|---|
| Hoffman & Kunze, *Linear Algebra* (2nd ed., 1971) | `IHUJ2G7R` | `IH2WQFQC` | `local-write-api-1783268640255-IHUJ2G7R_extracted.md` | extracted |
| Munkres, *Topology* (2nd ed., 2000) | `EEDYK7RG` | `CZQDCAJR` | `local-write-api-1783249491889-EEDYK7RG_extracted.md` | extracted |
| Hatcher, *Algebraic Topology* (2002) | `5UPFWXXF` | `QDLM25QY` | `Hatcher - 2002 - Algebraic Topology.md` | extracted |
| Dummit & Foote, *Abstract Algebra* (3rd ed., 2004) | `A4FFDNKB` | `XIINH8MK` | `local-write-api-1783380265761-A4FFDNKB_extracted.md` | extracted |
| Hungerford, *Algebra* (GTM 73, 1974) | `EW5CVTDL` | `D8B427XZ` | `local-write-api-1783337690991-EW5CVTDL_extracted.md` | extracted |
| Smith, *Algebra Course Notes* (843-1 through 845-3) | `LCYL45LE` | — | `assets/attachments/8000e.pdf` (vendored) | **PDF vendored; not attached in Zotero; 843–845 notes still missing** |

## Notes

- Hatcher's extraction was attached under a human-chosen title (`Hatcher - 2002 - Algebraic Topology.md`) rather than the loop's `<KEY>_extracted.md` convention.
- The Munkres extraction is complete: §12, §14, and §15 have no exercises in the book.
- Dummit & Foote has two PDF children: `A4FFDNKB_extracted.md` (MinerU extraction) and a second PDF titled `Abstract_algebra_fulltext`.
- Smith `LCYL45LE` is a `document` item with no children. The 12-page `8000e.pdf` packet is vendored at `assets/attachments/8000e.pdf` and referenced by the corpus card's provenance href; it is not yet attached to the Zotero item. The separate 843–845 course notes are a different document not yet in the library.
