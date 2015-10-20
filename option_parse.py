from optparse import OptionParser

parser = OptionParser()


parser.add_option("-p", "--page", dest="page",
                  help="the page to capture screenshot")
parser.add_option("-u", "--url", dest="url",
                  help="the url to capture screenshot")
parser.add_option("-m", "--maillist", dest="maillist",
                  help="the maillist to sent")
parser.add_option("-l", "--div_list", dest="div_list",
                  help="the div_list to capture")
parser.add_option("--type", dest="type")
parser.add_option("--platform", dest="platform")
parser.add_option("--version", dest="version")
parser.add_option("--year", dest="year")
parser.add_option("--ww", dest="ww")

(options, args) = parser.parse_args()

print options
