<template>
  <div class="container">
    <div class="detail-box">
      <!-- <p class="movie" style="text-align: left; margin-left: 10px;">No. {{ article?.id }}</p> -->
      <p class="movie" style="text-align: left; margin-left: 10px;">제목: {{ article?.title }}</p>
    
      <p class="movie" style="text-align: left; margin-left: 10px;">{{ article.username }} | {{ formatDateTime(article.created_at) }}</p>
      <p class="movie" style="text-align: left; margin-left: 10px;">마지막 작성시간: {{ formatDateTime(article.updated_at) }}</p>
    </div>

    <hr>
<!-- 
    <button class="like-btn">
      <div class="hand">
        <div class="thumb"></div>
      </div>
      <span>Like<span>{{ likeCount }}</span></span>
    </button> -->
    

    <div class="like-actions">
      <a class="btn-thumb" @click="toggleLike(article.id)">
        <i class="bi fs-3" :class="isLiked ? 'bi-hand-thumbs-up-fill' : 'bi-hand-thumbs-up'"></i>
        <!-- <i class="bi fs-3" :class="isLiked ? 'bi-heart-fill' : 'bi-heart'"></i> -->
      </a>
      <p>{{ likeCount }}</p>
    </div>

    <div class="content">
      <p>{{ article?.content }}</p>
    </div>

    <div class="actions">
      <button @click="updateArticleBtn" class="update-btn me-1">수정</button>
      <button @click="deleteArticle" class="delete-btn">삭제</button>
    </div>
    
    <hr>
    <div class="comment-box">
      <form @submit.prevent="createComment">

        <label for="content"></label>
        <textarea id="content" cols="30" rows="5" v-model="commentContent" placeholder="댓글을 입력하세요"></textarea><br>

        <button type="submit">댓글 작성</button>
      </form>
    </div>
    <br>
    <hr>

    <div class="comment-list">
      <div v-for="(comment,index) in commentList" :key="`${comment.id}-${index}`" class="comment-item">
      <p class="comment-username">{{ comment.username }}</p>
      <p class="comment-datetime">{{ formatDateTime(comment.created_at) }}</p>
      <p class="comment-content">{{ comment.content }}</p>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: '',
      commentContent: '',
      commentList: [],
      isLiked: false,
      likeCount: 0,
    }
  },
  created() {
    this.getArticleDetail()
    this.checkLikeStatus(this.$route.params.id)
    this.getCommentList()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then((res) => {
        // console.log(res)
        this.article = res.data 
      })
      .catch(err => console.log(err))
    },
    deleteArticle() {
      axios({
        method:'delete',
        url: `${API_URL}/api/v1/articles/${this.article.id}/`,
      })
      .then(() => {
        this.$router.push({ name:'community' })
      })
      .catch(err => console.log(err))
    },
    updateArticleBtn() {
      this.$router.push({ name:'UpdateView',params:{id:this.article.id}})
    },
    async createComment() {
      try {
        const token = this.$store.state.token.token
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
        const data = {
          content: this.commentContent,
        }
        await axios.post(`${API_URL}/api/v1/articles/${this.article.id}/comments/`,data,config)
        this.commentContent = ''
        await this.getCommentList()
      } catch (error) {
        console.error('Failed to create comment:', error)
      }
    },
    async getCommentList() {
      try {
        const token = this.$store.state.token.token
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
        const response = await axios.get(`${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,config)
        this.commentList = response.data
        console.log(this.commentList)
      } catch (error) {
        console.error('Failed to get comment list:', error)
      }
    },
    async toggleLike(articleId) {
      const previousLiked = this.isLiked;
      this.isLiked = !previousLiked;
      try{
        
        await this.articleLike(articleId)
        this.checkLikeStatus(articleId)

      } catch (error) {
        console.error('Failed to toggle like:', error)
        this.isLiked = previousLiked;
      }
    },
    async checkLikeStatus(articleId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        const response = await axios.get(`${API_URL}/api/v1/articles/${articleId}/like/`, config);
        console.log(response.data)
        this.isLiked = response.data.isLiked; // 좋아요 여부 업데이트
        this.likeCount = response.data.likeCount; // 좋아요 수 업데이트
        console.log(this.isLiked, this.likeCount)
      } catch (error) {
        console.error('Failed to check like status:', error);
      }
    },
    async articleLike(articleId) {
      try {
        const token = this.$store.state.token.token; // 토큰 가져오기
        const config = {
          headers: {
            Authorization: `Token ${token}`, // 헤더에 토큰 추가
          },
        };
        await axios.post(`${API_URL}/api/v1/articles/${articleId}/like/`, null, config);
      } catch (error) {
        console.error('Failed to like movie:', error);
      }
    },

    formatDateTime(dateTime) {
      return moment(dateTime).format('YYYY-MM-DD HH:mm:ss')
    }
  }
}
</script>

<style>
  
  .detail-box {
    margin-top: 20px;
  }
  .comment-box {
    border: 1px solid white;
    padding: 10px;
    margin-top: 20px;
    border-radius: 10px;
    /* background-color: #f5f5f5af; */
  }
  .comment-box label {
    font-weight: bold;
  }
  .comment-box textarea {
    width: 100%;
    resize: vertical;
    padding: 5px;
    border-radius: 10px;
    background-color: antiquewhite;
  }
  .comment-box button {
    background-color: darkgray;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 15px;
  }
  .comment-box button:hover {
    background-color: #45a049;
  }
  .comment-list {
    margin-top: 20px;
  }
  .comment-item {
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid white;
    color: white;

  }
  .comment-username {
    text-align: left;
    margin-bottom: 5px;
    color: white;
    font-weight: bold;
    font-size: 12px;
  }
  .comment-datetime {
    text-align: left;
    margin-bottom: 5px;
    color: white;
    font-size: 12px;
  }
  .comment-content {
    text-align: left;
    margin-bottom: 0;
    color: white;
    font-size: 16px;
  }
  .content {
    text-align: left;
    margin-left: 10px;
    margin-bottom: 20px;
    font-size: 18px;
    line-height: 1.5;
    color: white;
  }
  .actions {
    text-align: right;
  }
  .update-btn {
    background-color:darkgrey;
    color: white;
    border:none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 15px;
    font-size: 14px
  }
  .delete-btn {
    background-color:darkgrey;
    color: white;
    border:none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 15px;
    font-size: 14px
  }
  .like-actions {

    background-color: aliceblue;
    width: 70px;
    height: 70px;
    padding: 8px;
    border-radius: 50%;
    justify-content: flex-end;
    margin-left: auto;
  }
  .like-actions .btn-thumb {
    color:rgb(64, 47, 218);
    cursor: pointer;
    margin-left: 10px;
  }
</style>