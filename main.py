
##

import pandas as pd
from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_as_prq_wo_index as sprq

repo_url = 'https://github.com/imahdimir/d-Ticker-2-BaseTicker-map'

btic = 'BaseTicker'
tick = 'Ticker'

def main() :


  pass

  ##
  map_repo = GithubData(repo_url)
  map_repo.clone_overwrite_last_version()
  ##
  fpn = map_repo.data_fps[0]
  ##
  df = pd.read_parquet(fpn)
  ##
  df = df[[tick, btic]]
  ##
  df = df.applymap(norm)
  ##
  df = df.drop_duplicates()
  ##
  df = df.sort_values(btic)
  ##
  sprq(df , fpn)
  ##
  map_repo.commit_and_push_to_github_data_target('just sort with gov py')
  ##
  map_repo.rmdir()

  ##


  ##


##
# noinspection PyUnreachableCode
if False :

  pass

  ##


  ##

##