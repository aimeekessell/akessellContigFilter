/*
A KBase module: akessellContigFilter
This sample module contains one small method that filters contigs.
*/

module akessellContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_akessellContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        New app which filters contigs in an assembly using both a minimum and a maximum contig length
    */
    funcdef run_akessellContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
