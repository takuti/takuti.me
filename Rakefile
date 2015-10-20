namespace :preview do
  desc "Launch local preview environment"
  task :local do
    system "hugo server --watch"
  end

  desc "Generate public/ as production code (specifying baseUrl withou port)"
  task :production do
    system "direnv allow ."
    base_url = ENV["HUGO_BASE_URL"]
    system "hugo server --baseUrl='#{base_url}' --appendPort=false"
  end
end

namespace :rsync do
  system "direnv allow ."

  program = ENV["RSYNC_PROGRAM"]
  port = ENV["RSYNC_DEST_PORT"]
  user = ENV["RSYNC_USER"]
  host = ENV["RSYNC_HOST"]
  dest = ENV["RSYNC_DEST"]

  desc "--dry-run rsync"
    task :test do
      system "rsync --rsync-path=\"#{program}\" public/ -avz -e \"ssh -p #{port}\" -n --delete #{user}@#{host}:#{dest}"
    end
  desc "rsync"
    task :sync do
      system "rsync --rsync-path=\"#{program}\" public/ -avz -e \"ssh -p #{port}\" --delete #{user}@#{host}:#{dest}"
    end
end

namespace :converter do
  require "open-uri"
  require "json"
  require "kramdown"

  # convert tweet url to embedding html
  def embedding_tweet(content)
    embedded_content = content
    content.scan(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status\/([0-9]+)\/?)/).each do |url, id|
      tweet_json = open("https://api.twitter.com/1/statuses/oembed.json?id=#{id}").read
      tweet_html = JSON.parse(tweet_json, { :symbolize_names => true })[:html]
      embedded_content = embedded_content.gsub(/#{url}/, tweet_html)
    end
    embedded_content
  end

  desc "Converter: tweet urls -> twitter embedding card, Markdown+MathJax content -> html"
  task :content do
    Dir::glob("_content/note/*").each do |src|
      dst_path = src[1..-1].sub(/(.*)\.md/, '\1.html')
      next if File.exist?(dst_path)
      open(dst_path, "w") do |dst|
        puts dst_path
        content = open(src) { |f| f.read }
        content = content.sub(/(---.*---\n)/m, "")
        content = embedding_tweet(content)

        # write with concatinating front matter
        dst.write($1 + Kramdown::Document.new(content).to_html)
      end
    end
  end

  desc "Converter: sass -> css"
  task :style do
    system "sass -C --sourcemap=none _scss/style.scss static/style/style.css"
  end
end

task :convert => ["converter:content", "converter:style"]
task :default => ["convert", "preview:local"]
task :prepare => ["convert", "preview:production"]
