#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:([^\]]+)\])|(\[to:([^\]]+)\])|(-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1])/).flatten.compact.values_at(1,3,4).join(',')
