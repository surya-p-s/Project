package com.example.marinesoftapplication

import android.content.ContentValues
import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import com.google.android.material.navigation.NavigationBarItemView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

const val EXTRA_MESSAGE="com.example.marinesoftapplication.MESSAGE"
class UploadActivity : AppCompatActivity() {

    lateinit var imageView: ImageView
    lateinit var button: Button
    private val pickImage = 100
    private var imageUri: Uri?=null
    lateinit var upButton: Button

    private lateinit var auth : FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_upload)

        auth = Firebase.auth

        title="MarineSoft"
        imageView=findViewById(R.id.imageUploadView)
        button=findViewById(R.id.selectImgButton)
        upButton=findViewById(R.id.uplodImgButton)

//        Transfer data to data Page
        upButton.setOnClickListener {
            val speciesName=findViewById<EditText>(R.id.upSpeciesName)
            val name=speciesName.text.toString()
            val  intent=Intent(this,DataActivity::class.java).apply {
                putExtra(EXTRA_MESSAGE,name)
            }
            startActivity(intent)
        }


        button.setOnClickListener {
            val gallery=Intent(Intent.ACTION_PICK, MediaStore.Images.Media.INTERNAL_CONTENT_URI)
            startActivityForResult(gallery, pickImage)
        }
//        navigation

        val signOut=findViewById<NavigationBarItemView>(R.id.signOut)
        val graph=findViewById<NavigationBarItemView>(R.id.graph)
        val analytic=findViewById<NavigationBarItemView>(R.id.analytic)
        val upload=findViewById<NavigationBarItemView>(R.id.imageUpload)
        val home=findViewById<NavigationBarItemView>(R.id.home_menu)

        home.setOnClickListener {
            startActivity(Intent(this,DataActivity::class.java))
        }

        graph.setOnClickListener {
            startActivity(Intent(this,GraphActivity::class.java))
        }

        analytic.setOnClickListener {
            startActivity(Intent(this, AnalyticActivity::class.java))
        }
        // Authentiation
        signOut.setOnClickListener {
            Firebase.auth.signOut()
            updateUI()
        }
    }


    @Deprecated("Deprecated in Java")
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if(resultCode== RESULT_OK && requestCode==pickImage){
            imageUri=data?.data
            imageView.setImageURI(imageUri)
        }
    }
    private fun updateUI() {
        val intent= Intent(this,SignInPage::class.java)
        startActivity(intent)
        finish()
    }

}