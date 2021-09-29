/*
A KBase module: torbenContigFilter
This sample module contains one small method that filters contigs.
*/

module torbenContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_torbenContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    
    /*
        New app which filters contigs from an assembly using both minimum and maximum lengths.
    */

    funcdef run_torbenContigFilter_min_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};