#!/usr/bin/env ruby
puts ARGV[0].scan(/(\+\d{10})|(-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1])/).flatten.compact.join(',')
